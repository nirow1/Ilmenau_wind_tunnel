import threading
import logging
import struct

from socket import socket, AF_INET, SOCK_STREAM
from PySide6.QtCore import QThread, Signal
from time import sleep


class ScaleControl(QThread):
    SCALE_MEASUREMENTS = Signal(list)

    def __init__(self):
        super().__init__()
        self.ips = ["192.168.1.98", "192.168.1.97"]
        self.port = 23
        self.connected = False
        self.zero_values = [0, 0, 0, 0]

    def run(self):
        self._connect_to_scales()

    def _connect_to_scales(self):
        while not self.connected:
            try:
                self.zero_values = [0, 0, 0, 0]

                for ip in self.ips:
                    self.scales = socket(AF_INET, SOCK_STREAM)
                    self.scales.settimeout(1)
                    failed = self.scales.connect_ex((ip, self.port))
                    if not failed:
                        self.connected = True
                        self._start_communication()
                break
            except Exception as e:
                logging.getLogger().warning(f"{e}")
                sleep(5)

    def _start_communication(self):

        self.scales.send(b'AT+RAM_RW=8,1\x0d\x0a')
        self.scales.send(b'\x03')

        request_thread = threading.Thread(target=self._send_measure_request)
        request_thread.start()

        self._listen_to_tls()

    def _send_measure_request(self):
        while self.connected:
            sleep(0.1)
            self.scales.send(b'AT+RAM_RW=14,16,BIN,?\x0d\x0a')

    def _listen_to_tls(self):
        while self.connected:
            msg = self.scales.recv(1024)[23:39]
            self.scale_list = []
            if len(msg) == 16:
                self.scale_values = struct.unpack_from("<ffff", msg)
                for i in range(0, 4):
                    self.scale_list.append(float(self.scale_values[i])-self.zero_values[i])
                left_right_pressure = [round(self.scale_list[0] / 1000 * 9.81 / 3.23, 3),
                                       round((self.scale_list[0] + self.scale_list[1])/1000*9.81/2.81, 3),
                                       round((self.scale_list[2] - self.scale_list[3])/1000*9.81/2.81, 3),
                                       round((self.scale_list[2] + self.scale_list[3])/1000*9.81*0.06, 3)]
                self.SCALE_MEASUREMENTS.emit(left_right_pressure)

    def disconnect(self):
        try:
            self.connected = False
            sleep(0.2)
            self.scales.close()
            self.quit()
        except Exception as e:
            print(e)

    def set_zero_values(self):
        if self.connected:
            self.zero_values = [self.zero_values[i]+self.scale_list[i] for i in range(len(self.zero_values))]


if __name__ == '__main__':
    scales = ScaleControl()
    scales.run()
