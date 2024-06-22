from kb import KMKKeyboard
from kmk.extensions.media_keys import MediaKeys
from kmk.keys import KC
from kmk.modules.layers import Layers


media = MediaKeys()
layers = Layers()

keyboard = KMKKeyboard()
keyboard.extensions = [media]
keyboard.modules = [layers]
keyboard.extensions.append(keyboard.rgb)

keyboard.rgb.knight_effect_length = 8

keyboard.debug_enabled = False

keyboard.keymap = [
    [
        KC.LGUI(KC.N1), KC.LGUI(KC.N2), KC.LGUI(KC.N3),  KC.LGUI(KC.N4), KC.LGUI(KC.N5),  KC.LGUI(KC.N6), KC.MO(1), KC.AUDIO_VOL_UP,   
        KC.LALT(KC.N1), KC.LALT(KC.N2),  KC.LALT(KC.N3), KC.LALT(KC.N4), KC.LALT(KC.N5), KC.LALT(KC.N6), KC.UP, KC.AUDIO_VOL_DOWN,   
        KC.LSFT(KC.RCTL(KC.TAB)), KC.RCTL(KC.TAB), KC.RCTL(KC.F5),    KC.L,    KC.C,    KC.LEFT,    KC.ENTER,  KC.RIGHT,
        KC.N9, KC.N0, KC.X, KC.ESC, KC.M, KC.BSPC, KC.DOWN, KC.SPACE,  
    ],
    [
        KC.RGB_HUI, KC.RGB_SAI, KC.RGB_VAI,  KC.RGB_ANI, KC.RGB_TOG,  KC.RGB_TOG, KC.TRNS, KC.RGB_TOG,   
        KC.RGB_HUD, KC.RGB_SAD,  KC.RGB_VAD, KC.RGB_AND, KC.RGB_TOG, KC.RGB_TOG, KC.RGB_TOG, KC.RGB_TOG,   
        KC.RGB_M_P, KC.RGB_M_B, KC.RGB_M_R, KC.RGB_M_BR, KC.RGB_M_K, KC.RGB_M_S,    KC.RGB_TOG,  KC.RGB_TOG,
        KC.RGB_TOG, KC.RGB_TOG, KC.RGB_TOG, KC.RGB_TOG, KC.RGB_TOG, KC.RGB_TOG, KC.RGB_TOG, KC.RGB_TOG,  
    ],
]

if __name__ == '__main__':
    keyboard.go()
