
import board
from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.extensions.RGB import RGB


class KMKKeyboard(_KMKKeyboard):
    row_pins = (board.ROW0, board.ROW1, board.ROW2, board.ROW3)
    col_pins = (board.COL0, board.COL1, board.COL2, board.COL3, board.COL4, board.COL5, board.COL6, board.COL7)
    diode_orientation = DiodeOrientation.ROWS
    i2c = board.I2C
    # remove "val_default=0" to eneable rbg
    rgb = RGB(pixel_pin=board.NEOPIXEL, num_pixels=32, val_default=0)
