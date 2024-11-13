import struct
import time

from PySide6.QtCore import QThread, Signal
from threading import Thread
from snap7.logo import Logo
from time import sleep


class LogoControl(QThread):
    LOGO_DATA = Signal(list)

    def __init__(self):
        super().__init__()
        self.ip = "192.168.1.3"
        self.port = 512
        self.vfd = bytearray(b'\x05')
        self.connected = False
        self.sending = False

    def run(self):
        self._connect_to_logo()

    def _connect_to_logo(self):
        while not self.connected:
            try:
                self.logo = Logo()
                self.logo.connect(self.ip, 768, self.port)
                self.connected = True
                self.communication_thread = Thread(target=self._maintain_communication)
                self.communication_thread.start()
                sleep(0.05)
                self._start_reading_logo_data()
                break
            except Exception as e:
                print(e)
                sleep(5)

    def _start_reading_logo_data(self):
        while self.connected:
            if not self.sending:
                self.sending = True
                status_data = self.logo.db_read(0, 1, 1)
                status_data = self.byte_to_bits(status_data[0])
                sleep(0.001)
                byte_temps = self.logo.db_read(0, 4, 14)
                sleep(0.001)
                some_value = struct.unpack(">H",self.logo.db_read(0,20,2))
                self.sending = False
                temperatures = struct.unpack(">HHHHHHH", byte_temps)
                data = status_data[1:][::-1]
                data.append(temperatures[0])
                for i in range(1, 7):
                    data.append(temperatures[i]/10)
                data.append(round(some_value[0]/10, 1))

                self.LOGO_DATA.emit(data)
                sleep(0.1)
            else:
                sleep(0.05)

    def _maintain_communication(self):
        self.logo.db_write(0, 2, bytearray(b'\x02'))
        time.sleep(0.5)

        while self.connected:
            if not self.sending:
                self.sending = True
                self.logo.db_write(0, 2, bytearray(b'\x02'))
                self.sending = False
                sleep(2.5)
            else:
                sleep(0.05)

    def write_logo_value(self, pos: int, request: int):
        while self.connected:
            if not self.sending:
                hz_in_bytes = struct.pack('>H', request)
                self.sending = True
                self.logo.db_write(0, pos, bytearray(hz_in_bytes))
                self.sending = False
                break
            else:
                sleep(0.05)

    def write_logo_state(self, pos: int, message: bytes):
        while self.connected:
            if not self.sending:
                self.sending = True
                self.logo.db_write(0, pos, bytearray(message))
                self.sending = False
                break
            else:
                sleep(0.05)

    def change_vfd(self):
        if self.vfd == bytearray(b'\x05'):
            self.vfd = bytearray(b'\x07')
            self.send_vdf()
        else:
            self.vfd = bytearray(b'\x05')
            self.send_vdf()

    def send_vdf(self):
        while self.connected:
            if not self.sending:
                self.sending = True
                self.logo.db_write(0, 0, self.vfd)
                self.sending = False
                break
            else:
                sleep(0.05)

    @staticmethod
    def byte_to_bits(byte):
        return [(byte >> i) & 1 for i in range(7, -1, -1)]

    def disconnect(self):
        try:
            self.connected = False
            sleep(0.2)
            self.logo.disconnect()
            self.quit()
        except Exception as e:
            print(e)


if __name__ == '__main__':
    logo_communication = LogoControl()
    logo_communication.run()