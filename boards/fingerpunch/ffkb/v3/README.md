# Faux Fox Keyboard (ffkb) v3

![ffkb](https://fingerpunch.xyz/product/faux-fox-keyboard-v3)

A 36 or 42 key keyboard with support for per key LEDs, 2 rotary encoders (EC11
or evqwgd001), and a feature in the center (OLED (128x64), Cirque trackpad, or
PMW3360 trackball sensor).

Use `nice_nano/kb.py` when using a Nice!Nano v2 MCU.

> Note: The Nice!Nano doesn't have a lot of ROM, so there are a couple of extra
> steps. See guidance [over
> here](../../docs/Officially_Supported_Microcontrollers.md#nicenano).

An example `main.py` file is included for each MCU.

## Microcontroller support

Update this line in `kb.py` to any supported microcontroller in `kmk/quickpin/pro_micro`:

```python
from kmk.quickpin.pro_micro.boardsource_blok import pinout as pins
```
