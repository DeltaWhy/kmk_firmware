try:
    from typing import Optional, Tuple
except ImportError:
    pass
from collections import namedtuple
import kmk.handlers.stock as handlers
from kmk.keys import KC, FIRST_KMK_INTERNAL_KEY

from kmk.modules import Module

class AsetniopCombo(namedtuple('AsetniopCombo', ['keys', 'base', 'left_word', 'right_word', 'left_partials', 'right_partials'])):
    def __init__(self, keys, base, left_word=None, right_word=None, left_partials=None, right_partials=None):
        super().__init__(keys, base, left_word, right_word, left_partials, right_partials)

class Asetniop(Module):
    def __init__(self, combos=[]):
        self.combos = combos
        self._active = []
        self._held = []
        self._first = None
        self._shift = 0

    def during_bootup(self, keyboard):
        self.reset(keyboard)

    def before_matrix_scan(self, keyboard):
        return

    def after_matrix_scan(self, keyboard):
        return

    def before_hid_send(self, keyboard):
        return

    def after_hid_send(self, keyboard):
        return

    def on_powersave_enable(self, keyboard):
        return

    def on_powersave_disable(self, keyboard):
        return

    def process_key(self, keyboard, key: Key, is_pressed, int_coord):
        if key.code >= FIRST_KMK_INTERNAL_KEY:
            return key
        if is_pressed:
            return self.on_press(keyboard, key, int_coord)
        else:
            return self.on_release(keyboard, key, int_coord)

    def on_press(self, keyboard, key: Key, int_coord):
        if key == KC.LSFT:
            self._shift += 1
            if self._shift > 2:
                self._shift = 0
            print('press', key, self._shift)
            return key if self._shift else None
        if not self._active:
            self._first = int_coord
        self._active.append(key)
        self._held.append(key)
        print('press', key, self._first, self._active, self._held)

    def on_release(self, keyboard, key: Key, int_coord):
        if key == KC.LSFT:
            print('release', key, self._shift)
            return None if self._shift else key
        if len(self._active) == 1:
            self._active = []
            self._held = []
            self._first = None
            print('release', key, self._first, self._active, self._held)
            self.send_key(keyboard, key)
        else:
            if set(self._active) == set(self._held):
                # activate combo
                print('activate', self._active)
                self._held.remove(key)
                if not self.activate_combo(keyboard):
                    # key combo was invalid, treat it as a normal key release
                    keyboard.process_key(key, True)
                    keyboard._send_hid()
                    keyboard.process_key(key, False)
                    keyboard._send_hid()
                    self._active.remove(key)
                print('release', key, self._first, self._active, self._held)
            else:
                self._held.remove(key)
                if not self._held:
                    self._active = []
                    self._first = None
                print('release', key, self._first, self._active, self._held)

    def activate_combo(self, keyboard):
        for combo in self.combos:
            if set(self._active) == set(combo.keys):
                print(combo)
                if combo.base:
                    self.send_key(keyboard, combo.base)
                    return True
                elif self._first >= 0 and self._first <= 3:
                    if combo.left_word:
                        self.send_string(keyboard, combo.left_word + ' ')
                        return True
                    elif combo.right_word:
                        self.send_string(keyboard, combo.right_word + ' ')
                        return True
                elif self._first >= 4 and self._first <= 7:
                    if combo.right_word:
                        self.send_string(keyboard, combo.right_word + ' ')
                        return True
                    elif combo.left_word:
                        self.send_string(keyboard, combo.left_word + ' ')
                        return True
        return False

    def send_string(self, keyboard, string):
        for char in string:
            self.send_key(keyboard, KC[char])

    def send_key(self, keyboard, key):
        if key.code >= FIRST_KMK_INTERNAL_KEY:
            keyboard.pre_process_key(key, True)
            keyboard.pre_process_key(key, False)
            self.reset(keyboard)
            return
        if self._shift == 2:
            if key.code >= KC.A.code and key.code <= KC.Z.code:
                pass
            elif key.code in [KC.MINUS.code, KC.BSPC.code]:
                pass
            else:
                keyboard.process_key(KC.LSFT, False)
                self._shift = 0
        keyboard.process_key(key, True)
        keyboard._send_hid()
        keyboard.process_key(key, False)
        keyboard._send_hid()
        if self._shift == 1:
            keyboard.process_key(KC.LSFT, False)
            keyboard._send_hid()
            self._shift = 0

    def reset(self, keyboard):
        self._active = []
        self._held = []
        self._first = None
