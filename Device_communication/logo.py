import threading
import struct
import time

from PySide6.QtCore import QThread, Signal
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
                self.communication_thread = threading.Thread(target=self._maintain_communication)
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
                logo_data = self.logo.db_read(0, 2, 2)
                sleep(0.001)
                logo_data += self.logo.db_read(0, 6, 2)
                logo_data = struct.unpack(">HH", logo_data)
                self.sending = False
                data = [logo_data[0] / 10, round(((logo_data[1] - 446) * -1) / 12.55, 2)]
                self.LOGO_DATA.emit(data)
                sleep(0.1)
            else:
                sleep(0.05)

    def _maintain_communication(self):
        self.logo.db_write(0, 0, bytearray(b'\x04'))
        time.sleep(0.5)

        while self.connected:
            if not self.sending:
                self.sending = True
                self.logo.db_write(0, 0, self.vfd)
                self.sending = False
                sleep(4)
            else:
                sleep(0.05)

    def write_logo_data(self, requested_hz: int):
        while self.connected:
            if not self.sending:
                hz_in_bytes = struct.pack('>H', requested_hz)
                self.sending = True
                self.logo.db_write(0, 4, bytearray(hz_in_bytes))
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