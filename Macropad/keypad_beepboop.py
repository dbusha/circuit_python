class BeepBoopKeyPad:
    macropad = None
    tones = [196, 220, 246, 262, 294, 330, 349, 392, 440, 494, 523, 587]

    def __init__(self, macropad):
        self.macropad = macropad

    def process_key_input(self, key_number, is_pressed):
        if is_pressed:
            self.macropad.start_tone(self.tones[key_number])
            #self.macropad.pixels[key_number] = colorwheel(int(255 / 12) * key_number)
        else:
            self.macropad.stop_tone()
            self.macropad.pixels.fill((0,0,0))


    def process_encoder_input(self, position, last_position):
        print("postion: " + str(position) + ". last: " + str(last_position))


    def color_keypad(self):
        pass


    def get_description(self):
        return "BeepBoop!"