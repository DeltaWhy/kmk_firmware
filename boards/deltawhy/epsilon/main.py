print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.keypad import KeysScanner
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from asetniop import Asetniop

keyboard = KMKKeyboard()
keyboard.col_pins = (board.D0, board.D1, board.D2, board.D3)
keyboard.row_pins = (board.D7, board.D8, board.D9)
keyboard.diode_orientation = DiodeOrientation.COL2ROW
keyboard.modules.append(Layers())

from dictionaries import COLEMAK_COMBOS

#asetniop = Asetniop(COLEMAK_COMBOS + COLEMAK_WORDS)
asetniop = Asetniop(COLEMAK_COMBOS)
keyboard.modules.append(asetniop)

# _KEY_CFG = [
#        board.A0, board.A1, board.A2, board.A3,
#        board.D2, board.D3, board.D4, board.D5,
#        board.D10, board.D9
# ]
#
# keyboard.matrix = KeysScanner(
#        pins=_KEY_CFG,
#        value_when_pressed=False,
#        pull=True,
#        interval=0.02,
#        max_events=64)

# keyboard.keymap = [
#     [KC.A, KC.S, KC.E, KC.T,    KC.N, KC.I, KC.O, KC.P,
#                        KC.LSFT, KC.SPC]
# ]


keyboard.keymap = [
    [KC.A, KC.R, KC.S, KC.T,    KC.N, KC.E, KC.I, KC.O,
                       KC.LSFT, KC.SPC],
    [KC.N1, KC.N2, KC.N3, KC.N4,   KC.N7, KC.N8, KC.N9, KC.N0,
                          KC.LSFT, KC.SPC],
]

if __name__ == '__main__':
    keyboard.go()
