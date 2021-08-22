class AudioKeyPad:
    macropad = None
    command_map = None

    def __init__(self, macropad):
        self.macropad = macropad
        self.command_map = { 
            0: self.macropad.ConsumerControlCode.MUTE,
            2: self.macropad.ConsumerControlCode.PLAY_PAUSE,
            5: self.macropad.ConsumerControlCode.SCAN_PREVIOUS_TRACK,
            7: self.macropad.ConsumerControlCode.SCAN_NEXT_TRACK            
        }

    def process_key_input(self, key_number, is_pressed):
        self.parse_key_code(key_number)


    def parse_key_code(self, key_number):
        if key_number not in self.command_map.keys():
            return
        self.macropad.consumer_control.send(self.command_map[key_number])


    def process_encoder_input(self, position, last_position):
        print("postion: " + str(position) + ". last: " + str(last_position))
        if position is not None and last_position is not None and position < last_position:
            for _ in range(1,3):
                self.macropad.consumer_control.send(self.macropad.ConsumerControlCode.VOLUME_DECREMENT)
        elif position is not None and last_position is not None and position > last_position:
            for _ in range(1,3):
                self.macropad.consumer_control.send(self.macropad.ConsumerControlCode.VOLUME_INCREMENT)

    def color_keypad(self):
        self.macropad.pixels.brightness = 0.5
        self.macropad.pixels[0] = (0,0,0)
        self.macropad.pixels[1] = (0,0,0)
        self.macropad.pixels[2] = (0,255,0)
        self.macropad.pixels[3] = (0,0,0)
        self.macropad.pixels[4] = (0,0,0)
        self.macropad.pixels[5] = (126,0,126)
        self.macropad.pixels[6] = (0,0,0)
        self.macropad.pixels[7] = (126,0,126)
        self.macropad.pixels[8] = (0,0,0)
        self.macropad.pixels[9] = (0,0,0)
        self.macropad.pixels[10] = (0,0,0)
        self.macropad.pixels[11] = (0,0,0)

    def get_description(self):
        return "Audio"