import adafruit_74hc595
import board
import busio
import digitalio

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.scanners.digitalio import MatrixScanner
from kmk.quickpin.pro_micro.nice_nano import pinout


class KMKKeyboard(_KMKKeyboard):
    diode_orientation = DiodeOrientation.COLUMNS
    rgb_pixel_pin = board.P0_06
    rgb_num_pixels = 42
    i2c = board.I2C
    spi = busio.SPI(pinout[15], MOSI=pinout[13]) # , MISO=pinout[14])
    
    while not spi.try_lock():
        pass
    spi.configure(baudrate=200000)
    spi.unlock()

    sr_latchpin = digitalio.DigitalInOut(pinout[12])
    sr = adafruit_74hc595.ShiftRegister74HC595(spi, sr_latchpin)

    col_pins = (1, 0, 2, 4, 3, 5, 6, 7)
    row_pins = (
            pinout[1],
            pinout[19],
            pinout[18],
            pinout[17],
            pinout[16],
            pinout[6]
    )

# flake8: noqa
    coord_mapping = [
       0,   1,  2,  3,  4,  5,      6,  7, 35, 28, 37, 31,
       8,   9, 10, 11, 12, 13, 33, 14, 15, 26, 36, 29, 39,
       16, 17, 18, 19, 20, 21,     22, 23, 34, 27, 30, 38,
       41,         43, 44, 45,     46, 47, 42,         40,
        ]

    def __init__(self, *args, **kwargs):
        self.matrix = MatrixScanner(
                cols = [self.sr.get_pin(i) for i in self.col_pins],
                rows = self.row_pins,
                diode_orientation = self.diode_orientation,
                )
        #self._rows = [digitalio.DigitalInOut(pin) for pin in self.row_pins]
        #self._cols = [self.sr.get_pin(i) for i in [1, 0, 2, 4, 3, 5, 6, 7]]

    def read_rows(self):
        return [row.value for row in self._rows]

    def write_cols(self, values):
        if len(values) != 8:
            raise KeyError('length must be 8')
        for i in range(8):
            self._cols[i].value = values[i]

encoder_pins = ((pinout[7], pinout[8], None),(pinout[9], pinout[10], None))
