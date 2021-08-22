from adafruit_macropad import MacroPad
from macropad_display import MacroPadDisplay
from keypad_num import NumPad
from keypad_debugger import DebuggerKeyPad
from keypad_audio import AudioKeyPad
from keypad_navigate import NavKeyPad
from keypad_beepboop import BeepBoopKeyPad

last_position = None

macropad = MacroPad(rotation=90)
num_pad = NumPad(macropad)
display = MacroPadDisplay(macropad)
audio = AudioKeyPad(macropad)
debugger = DebuggerKeyPad(macropad, display)
nav_pad = NavKeyPad(macropad)
beep_boop = BeepBoopKeyPad(macropad)


class Modes():
    NUM_PAD = 0
    DEBUG = 1
    AUDIO = 2
    NAVIGATE = 3
    BEEP_BOOP = 3

mode_map = {
    Modes.NUM_PAD: num_pad,
    Modes.DEBUG: debugger,
    Modes.AUDIO: audio,
    Modes.NAVIGATE: nav_pad,
    Modes.BEEP_BOOP: beep_boop
}

mode = Modes.NUM_PAD
current_mode = num_pad

num_pad.color_keypad()
display.set_description(num_pad.get_description())

#-----------------------------------------------------------------------

while True:
    has_input = False
        
    macropad.encoder_switch_debounced.update()
    if macropad.encoder_switch_debounced.pressed:
        mode = (mode + 1) % 4
        current_mode = mode_map[mode]
        position = 0
        has_input = True 
    else:
        position = macropad.encoder
        if position != last_position:
            has_input = True
            current_mode.process_encoder_input(position, last_position)
            last_position = position

    key_event = macropad.keys.events.get()
    if key_event:
        has_input = True
        current_mode.process_key_input(key_event.key_number, key_event.pressed)

    display.update_sleep_count(has_input)    
        
    if display.is_sleeping == True:
        display.color_keypad()
    else:
        display.set_description(current_mode.get_description())
        display.update_position(position)
        current_mode.color_keypad()

    display.write_to_display()
    