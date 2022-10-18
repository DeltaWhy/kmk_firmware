import board

import kb

from kmk.extensions.media_keys import MediaKeys
from kmk.keys import KC
from kmk.modules.combos import Combos, Sequence
from kmk.modules.dynamic_sequences import DynamicSequences
from kmk.modules.encoder import EncoderHandler
from kmk.modules.layers import Layers
from kmk.modules.mouse_keys import MouseKeys
from kmk.modules.oneshot import OneShot

combos = Combos()
dyn_seq = DynamicSequences(
    slots=1, # The number of sequence slots to use
    timeout=60000,  # Maximum time to spend in record or config mode before stopping automatically, milliseconds
    key_interval=20,  # Milliseconds between key events while playing
    use_recorded_speed=False,  # Whether to play the sequence at the speed it was typed
)
layers = Layers()
oneshot = OneShot()
media_keys = MediaKeys()

encoder_handler = EncoderHandler()
encoder_handler.pins = kb.encoder_pins

keyboard = kb.KMKKeyboard()
keyboard.modules = [combos, dyn_seq, layers, oneshot, encoder_handler]
keyboard.modules.append(MouseKeys())
keyboard.extensions = [media_keys]
keyboard.debug_enabled = False

# Convenience variables for the Keymap
_______ = KC.TRNS
xxxxxxx = KC.NO

ZOOM_IN = KC.LCTRL(KC.EQUAL)
ZOOM_OUT = KC.LCTRL(KC.MINUS)

L1_TAB = KC.LT(1, KC.TAB, prefer_hold=True)
L2_ENT = KC.LT(2, KC.ENT, prefer_hold=True)

OS_LSFT = KC.OS(KC.LSFT)

SEQ_REC = KC.RECORD_SEQUENCE()
SEQ_STP = KC.STOP_SEQUENCE()
SEQ_PLY = KC.PLAY_SEQUENCE()

combos.combos = [
    Sequence((KC.LEADER, KC.A), KC.LCTL(KC.A)),  # select All
    Sequence((KC.LEADER, KC.T), KC.LCTL(KC.X)),  # cuT
    Sequence((KC.LEADER, KC.C), KC.LCTL(KC.C)),  # Copy
    Sequence((KC.LEADER, KC.P), KC.LCTL(KC.V)),  # Paste
    Sequence((KC.LEADER, KC.U), KC.LCTL(KC.Z)),  # Undo
    Sequence((KC.LEADER, KC.Y), KC.LCTL(KC.Y)),  # redo
    ]

# flake8: noqa
keyboard.keymap = [
    [  # 0: Colemak-DH letters
        KC.ESC,  KC.Q,    KC.W,    KC.F,    KC.P,    KC.B,             KC.J,    KC.L,    KC.U,    KC.Y,    KC.SCLN, KC.LEADER,
        KC.LCTL, KC.A,    KC.R,    KC.S,    KC.T,    KC.G,    xxxxxxx, KC.M,    KC.N,    KC.E,    KC.I,    KC.O,    KC.QUOT,
        KC.LALT, KC.Z,    KC.X,    KC.C,    KC.D,    KC.V,             KC.K,    KC.H,    KC.COMM, KC.DOT,  KC.SLSH, KC.BSLS,
                 xxxxxxx,          KC.LGUI, OS_LSFT, KC.BSPC,          L1_TAB,    KC.SPACE,L2_ENT,             xxxxxxx,
    ],
    [  # 1: Nav & Numbers
        KC.TAB,  KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,            KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,   KC.DEL,
        _______, KC.LPRN, KC.LEFT, KC.UP,   KC.RIGHT,KC.RPRN, _______, KC.GRV,  KC.PLUS, KC.EQL,  xxxxxxx, xxxxxxx, xxxxxxx,
        _______, KC.LBRC, KC.LCBR, KC.DOWN, KC.RCBR, KC.RBRC,          KC.TILD, KC.MINS, KC.UNDS, xxxxxxx, xxxxxxx, xxxxxxx,
                 _______,          _______, _______, KC.DEL,           _______, _______, _______, _______,
    ],
    [  # 2: F-row & Board Functions
        KC.F12,  KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,            KC.F6,   KC.F7,   KC.F8,   KC.F9,    KC.F10,  KC.F11,
        _______, SEQ_REC, SEQ_PLY, _______, _______, _______, _______, _______, _______, _______, _______,  _______, _______,
        _______, SEQ_STP, _______, _______, _______, _______,          _______, _______, _______, _______,  _______, _______,
                 _______,          _______, _______, _______,          _______, _______, _______,           _______, 
    ],
]

encoder_handler.map = [
    ((KC.VOLD, KC.VOLU, KC.MUTE), (KC.MW_UP, KC.MW_DN, _______)),  # Layer 1
    ((ZOOM_OUT, ZOOM_IN, _______), (KC.UP, KC.DOWN, _______)),  # Layer 2
    ((_______, _______, _______), (_______, _______, _______)),  # Layer 3
    ((_______, _______, _______), (_______, _______, _______)),  # Layer 4
    ((_______, _______, _______), (_______, _______, _______)),  # Layer 5
    ((_______, _______, _______), (_______, _______, _______)),  # Layer 6
]

if __name__ == '__main__':
    keyboard.go()
