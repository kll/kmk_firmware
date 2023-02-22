import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner

# GPIO to key mapping - each line is a new row.
_KEY_CFG = [
    board.KEY1,  board.KEY2,  board.KEY3,
    board.KEY4,  board.KEY5,  board.KEY6,
    board.KEY7, board.KEY8, board.KEY9,
    board.KEY10,  board.KEY11,  board.KEY12,
]


# Keyboard implementation class
class MyKeyboard(KMKKeyboard):
    def __init__(self):
        # create and register the scanner
        self.matrix = KeysScanner(
            # require argument:
            pins=_KEY_CFG,
            # optional arguments with defaults:
            value_when_pressed=False,
            pull=True,
            interval=0.02,  # Debounce time in floating point seconds
            max_events=64
        )
