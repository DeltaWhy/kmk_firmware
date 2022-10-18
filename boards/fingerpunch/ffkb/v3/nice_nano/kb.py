import board
import busio
from digitalio import DigitalInOut

from adafruit_74hc595 import ShiftRegister74HC595

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.quickpin.pro_micro.nice_nano import pinout as pins
from kmk.scanners import DiodeOrientation
from kmk.scanners.digitalio import MatrixScanner


class KMKKeyboard(_KMKKeyboard):
    col_pins = (1, 0, 2, 4, 3, 5, 6, 7)
    row_pins = (
            pins[1],
            pins[19],
            pins[18],
            pins[17],
            pins[16],
            pins[6]
    )
    diode_orientation = DiodeOrientation.COLUMNS
    rgb_pixel_pin = pins[0]
    rgb_num_pixels = 42
    i2c = board.I2C
    spi = busio.SPI(pins[15], MOSI=pins[13]) # , MISO=pins[14])
    sr_latchpin = DigitalInOut(pins[12])
    sr = ShiftRegister74HC595(spi, sr_latchpin)

    # flake8: noqa
    # fmt: off
    coord_mapping = [
       0,   1,  2,  3,  4,  5,      6,  7, 35, 28, 37, 31,
       8,   9, 10, 11, 12, 13, 33, 14, 15, 26, 36, 29, 39,
       16, 17, 18, 19, 20, 21,     22, 23, 34, 27, 30, 38,
       41,         43, 44, 45,     46, 47, 42,         40,
        ]

    def __init__(self, *args, **kwargs):
        while not self.spi.try_lock():
            pass
        self.spi.configure(baudrate=200000)
        self.spi.unlock()

        self.matrix = MatrixScanner(
                cols = [self.sr.get_pin(i) for i in self.col_pins],
                rows = self.row_pins,
                diode_orientation = self.diode_orientation,
        )

encoder_pins = ((pins[7], pins[8], None),(pins[9], pins[10], None))
