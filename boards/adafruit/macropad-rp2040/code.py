print("Starting")

import board

from kb import MyKeyboard
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.RGB import RGB, AnimationModes
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler

keyboard = MyKeyboard()
encoder_handler = EncoderHandler()
keyboard.modules = [encoder_handler]

underglow = RGB(
    pixel_pin=board.NEOPIXEL,
    num_pixels=12,
    val_limit=100,
    val_default=25,
    animation_mode=AnimationModes.RAINBOW,
)
keyboard.extensions.append(underglow)

media_keys = MediaKeys()
keyboard.extensions.append(media_keys)

keyboard.keymap = [
    [
        KC.P7, KC.P8, KC.P9,
        KC.P4, KC.P5, KC.P6,
        KC.P1, KC.P2, KC.P3,
        KC.ESC, KC.P0, KC.PDOT,
    ]
]

encoder_handler.pins = ((board.ENCODER_A, board.ENCODER_B, board.ENCODER_SWITCH, False),)
encoder_handler.map = [ ((KC.VOLU, KC.VOLD, KC.MPLY),), ]

if __name__ == '__main__':
    keyboard.go()
