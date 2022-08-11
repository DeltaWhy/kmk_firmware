from kmk.keys import Key, KC
from asetniop import AsetniopCombo

QWERTY_COMBOS = [
    AsetniopCombo((KC.A, KC.S), KC.W),
    AsetniopCombo((KC.A, KC.E), KC.X),
    AsetniopCombo((KC.A, KC.T), KC.F),
    AsetniopCombo((KC.A, KC.N), KC.Q),
    AsetniopCombo((KC.A, KC.I), KC.Z),
    AsetniopCombo((KC.A, KC.O), KC.LBRACKET),
    AsetniopCombo((KC.A, KC.P), KC.SLASH),

    AsetniopCombo((KC.S, KC.E), KC.D),
    AsetniopCombo((KC.S, KC.T), KC.C),
    AsetniopCombo((KC.S, KC.N), KC.J),
    AsetniopCombo((KC.S, KC.I), KC.K),
    AsetniopCombo((KC.S, KC.O), KC.DOT),
    AsetniopCombo((KC.S, KC.P), KC.RBRACKET),

    AsetniopCombo((KC.E, KC.T), KC.R),
    AsetniopCombo((KC.E, KC.N), KC.Y),
    AsetniopCombo((KC.E, KC.I), KC.COMMA),
    AsetniopCombo((KC.E, KC.O), KC.MINUS),
    AsetniopCombo((KC.E, KC.P), KC.QUOTE),

    AsetniopCombo((KC.T, KC.N), KC.B),
    AsetniopCombo((KC.T, KC.I), KC.V),
    AsetniopCombo((KC.T, KC.O), KC.G),
    AsetniopCombo((KC.T, KC.P), KC.BSPC),

    AsetniopCombo((KC.N, KC.I), KC.H),
    AsetniopCombo((KC.N, KC.O), KC.U),
    AsetniopCombo((KC.N, KC.P), KC.M),

    AsetniopCombo((KC.I, KC.O), KC.L),
    AsetniopCombo((KC.I, KC.P), KC.N1),  # !@

    AsetniopCombo((KC.O, KC.P), KC.SCLN),

    AsetniopCombo((KC.A, KC.S, KC.E, KC.T), KC.TAB),
    AsetniopCombo((KC.N, KC.I, KC.O, KC.P), KC.ENTER),
]

COLEMAK_COMBOS = [
    AsetniopCombo((KC.A, KC.R), KC.W),
    AsetniopCombo((KC.A, KC.S), KC.X),
    AsetniopCombo((KC.A, KC.T), KC.P),
    AsetniopCombo((KC.A, KC.N), KC.J),
    AsetniopCombo((KC.A, KC.E), KC.Q),
    AsetniopCombo((KC.A, KC.I), KC.LBRACKET),  # [(
    AsetniopCombo((KC.A, KC.O), KC.BSPC),

    AsetniopCombo((KC.R, KC.S), KC.F),
    AsetniopCombo((KC.R, KC.T), KC.C),
    AsetniopCombo((KC.R, KC.N), KC.K),
    AsetniopCombo((KC.R, KC.E), KC.Z),
    AsetniopCombo((KC.R, KC.I), KC.DOT),
    AsetniopCombo((KC.R, KC.O), KC.RBRACKET),  # )]

    AsetniopCombo((KC.S, KC.T), KC.D),
    AsetniopCombo((KC.S, KC.N), KC.M),
    AsetniopCombo((KC.S, KC.E), KC.COMMA),
    AsetniopCombo((KC.S, KC.I), KC.MINUS),
    AsetniopCombo((KC.S, KC.O), KC.QUOTE),

    AsetniopCombo((KC.T, KC.N), KC.B),
    AsetniopCombo((KC.T, KC.E), KC.V),
    AsetniopCombo((KC.T, KC.I), KC.G),
    AsetniopCombo((KC.T, KC.O), KC.SLASH),

    AsetniopCombo((KC.N, KC.E), KC.H),
    AsetniopCombo((KC.N, KC.I), KC.Y),
    AsetniopCombo((KC.N, KC.O), KC.L),

    AsetniopCombo((KC.E, KC.I), KC.U),
    AsetniopCombo((KC.E, KC.O), KC.N1),  # !@

    AsetniopCombo((KC.I, KC.O), KC.SCLN),

    AsetniopCombo((KC.A, KC.R, KC.S, KC.T), KC.TAB),
    AsetniopCombo((KC.N, KC.E, KC.I, KC.O), KC.ENTER),

    AsetniopCombo((KC.N3, KC.N4), KC.N5),
    AsetniopCombo((KC.N7, KC.N8), KC.N6),

    AsetniopCombo((KC.A, KC.T, KC.N, KC.O), KC.TG(1)),
    AsetniopCombo((KC.N1, KC.N4, KC.N7, KC.N0), KC.TG(1)),
]

COLEMAK_WORDS = [
    AsetniopCombo((KC.A, KC.R, KC.S), None, 'was', None, ('was', 'fa', 'af', 'ars', 'ws', 'sw', 'far', 'fra', 'saw', 'aff', 'ras', 'fas', 'sar', 'rsa', 'ssar', 'saf', 'afr', 'aws', 'raf', 'rass'), None),
    AsetniopCombo((KC.A, KC.R, KC.T), None, 'part', None, ('ca', 'ac', 'pr', 'art', 'par', 'act', 'tra', 'tw', 'rat', 'car', 'part', 'tar', 'rac', 'rta', 'cat', 'acc', 'rp', 'wat', 'ract', 'atc'), None),
    AsetniopCombo((KC.A, KC.S, KC.T), None, 'past'),
    AsetniopCombo((KC.R, KC.S, KC.T), None, 'dr'),
    AsetniopCombo((KC.A, KC.R, KC.S, KC.T), None, 'fact'),
    AsetniopCombo((KC.A, KC.R, KC.N), None, 'ran'),
    AsetniopCombo((KC.A, KC.S, KC.N), None, 'am', 'man'),
    AsetniopCombo((KC.R, KC.S, KC.N), None, None, 'mr'),
    AsetniopCombo((KC.A, KC.R, KC.S, KC.N), None, 'ask', 'mark'),
    AsetniopCombo((KC.A, KC.T, KC.N), None, None, 'japan'),
    AsetniopCombo((KC.A, KC.R, KC.T, KC.N), None, 'can'),
    AsetniopCombo((KC.A, KC.S, KC.T, KC.N), None, 'and'),
    AsetniopCombo((KC.A, KC.R, KC.S, KC.T, KC.N), None, 'dark'),
    AsetniopCombo((KC.A, KC.R, KC.E), None, 'were'),
    AsetniopCombo((KC.S, KC.E), KC.COMMA, 'see'),
    AsetniopCombo((KC.A, KC.S, KC.E), None, 'sea', 'ease'),
    AsetniopCombo((KC.R, KC.S, KC.E), None, 'free'),
    AsetniopCombo((KC.A, KC.R, KC.S, KC.E), None, 'few'),
    AsetniopCombo((KC.A, KC.T, KC.E), None, 'tea', 'eat'),
    AsetniopCombo((KC.R, KC.T, KC.E), None, None, 'ever'),
    AsetniopCombo((KC.A, KC.R, KC.T, KC.E), None, 'water'),
    AsetniopCombo((KC.S, KC.T, KC.E), None, 'set'),
    AsetniopCombo((KC.A, KC.S, KC.T, KC.E), None, 'state', 'east'),
    AsetniopCombo((KC.R, KC.S, KC.T, KC.E), None, 'street', 'effect'),
    AsetniopCombo((KC.A, KC.R, KC.S, KC.T, KC.E), None, 'after'),
    AsetniopCombo((KC.A, KC.N, KC.E), None, 'anne', 'jane'),
    AsetniopCombo((KC.R, KC.N, KC.E), None, None, 'her'),
    AsetniopCombo((KC.A, KC.R, KC.N, KC.E), None, 'when', 'new'),
    AsetniopCombo((KC.S, KC.N, KC.E), None, 'she', 'me'),
    AsetniopCombo((KC.A, KC.S, KC.N, KC.E), None, 'same', 'has'),
    AsetniopCombo((KC.R, KC.S, KC.N, KC.E), None, 'fresh', 'mere'),
    AsetniopCombo((KC.A, KC.R, KC.S, KC.N, KC.E), None, None, 'make'),
    AsetniopCombo((KC.T, KC.N, KC.E), None, 'the'),
    AsetniopCombo((KC.A, KC.T, KC.N, KC.E), None, 'that', 'have'),
    AsetniopCombo((KC.R, KC.T, KC.N, KC.E), None, 'there', 'never'),
    AsetniopCombo((KC.A, KC.R, KC.T, KC.N, KC.E), None, 'what'),
    AsetniopCombo((KC.S, KC.T, KC.N, KC.E), None, 'them'),
    AsetniopCombo((KC.A, KC.S, KC.T, KC.N, KC.E), None, None, 'had'),
    AsetniopCombo((KC.R, KC.S, KC.T, KC.N, KC.E), None, 'remember', 'members'),
    AsetniopCombo((KC.A, KC.R, KC.S, KC.T, KC.N, KC.E), None, 'came', 'heard'),
]
