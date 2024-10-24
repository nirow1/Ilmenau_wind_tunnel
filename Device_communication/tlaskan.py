import threading
import logging
import numpy
import time

from socket import socket, AF_INET, SOCK_STREAM
from PySide6.QtCore import Signal, QThread


class TlaskanControl(QThread):
    TLASKAN_DATA = Signal(list)

    def __init__(self):
        super().__init__()
        self.port = 23
        self.connected = False
        self.ip = "192.168.1.96"
        self.tlaskan_data = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        self.zero_velocity = 0

    def run(self):
        self._connect_to_tlaskan()

    def _connect_to_tlaskan(self):
        while not self.connected:
            try:
                self.tlaskan = socket(AF_INET, SOCK_STREAM)
                self.tlaskan.connect((self.ip, self.port))
                self.connected = True
                self._start_communication()
                break
            except Exception as e:
                logging.getLogger().warning(f"{e}")
                time.sleep(5)

    def _start_communication(self):
        request_thread = threading.Thread(target=self._send_measure_request)
        request_thread.start()
        self._listen_to_tls()

    def _send_measure_request(self):
        while self.connected:
            time.sleep(0.1)
            self.tlaskan.send(b'AT+ONE_MEASURE=0\x0d\x0a')

    def _listen_to_tls(self):
        while self.connected:
            msg = self.tlaskan.recv(1024)
            msg = (msg[18:].replace(b';NORMAL', b'')
                   .replace(b'; NORMAL', b'')
                   .replace(b'; inH20', b'')
                   .replace(b'\r\n', b'')
                   .split(b';'))
            del msg[-1:]

            if len(msg) != 0:
                self.tlaskan_data[2] = float(msg[0].decode('utf-8'))  # ATM_TEMP
                self.tlaskan_data[1] = float(msg[1].decode('utf-8'))  # ATM_PRESS
                self.tlaskan_data[0] = float(msg[2].decode('utf-8'))  # ATM_HUM
                self.tlaskan_data[3] = round((float(msg[3].decode()) * 249.174 - self.zero_velocity), 3)  # DIF_PRESS

                rh = self.tlaskan_data[0]
                p_bar = self.tlaskan_data[1]
                ta_s = self.tlaskan_data[2]
                dp = self.tlaskan_data[3]

                if dp < 0:
                    dp = 0
                try:
                    pv = numpy.exp(23.58 - (4044.2 / (235.6 + ta_s)))
                    rho = 1.316 * 0.001 / (ta_s + 273.15) * (2.65 * p_bar - (rh / 100) * pv)
                    velocity = 1.3974 * ((dp / rho) ** (1 / 2))
                    self.tlaskan_data[4] = round(velocity, 3)
                    self.tlaskan_data[5] = rho
                except Exception as e:
                    print(e)
                finally:
                    self.TLASKAN_DATA.emit(self.tlaskan_data)

    def set_zero_value(self):
        if self.connected:
            self.zero_velocity += self.tlaskan_data[3]

    def disconnect(self):
        try:
            self.connected = False
            time.sleep(0.2)
            self.tlaskan.close()
            self.quit()
        except Exception as e:
            print(e)
