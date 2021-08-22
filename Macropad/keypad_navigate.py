class NavKeyPad:
    macropad = None
    command_map = None

    def __init__(self, macropad):
        self.macropad = macropad
        self.command_map = { 
            1: self.macropad.Keycode.HOME,
            3: self.macropad.Keycode.PAGE_UP,
            5: self.macropad.Keycode.END,
            6: self.macropad.Keycode.UP_ARROW,
            7: self.macropad.Keycode.PAGE_DOWN,
            9: self.macropad.Keycode.LEFT_ARROW,
            10: self.macropad.Keycode.DOWN_ARROW,
            11: self.macropad.Keycode.UP_ARROW            
        }

    def process_key_input(self, key_number, is_pressed):
        self.parse_key_code(key_number)


    def parse_key_code(self, key_number):
        if key_number not in self.command_map.keys():
            return
        self.macropad.keyboard.send(self.command_map[key_number])


    def process_encoder_input(self, position, last_position):
        if position is not None and last_position is not None and position < last_position:         
            self.macropad.keyboard.send(self.macropad.Keycode.LEFT_ARROW)
        elif position is not None and last_position is not None and position > last_position:
            self.macropad.keyboard.send(self.macropad.Keycode.RIGHT_ARROW)


    def color_keypad(self):
        self.macropad.pixels.brightness = 0.3
        self.macropad.pixels[0] = (0,0,0)
        self.macropad.pixels[1] = (0,0,0)
        self.macropad.pixels[2] = (0,0,0)
        self.macropad.pixels[3] = (0,0,0)
        self.macropad.pixels[4] = (0,0,0)
        self.macropad.pixels[5] = (0,0,0)
        self.macropad.pixels[6] = (0,0,255)
        self.macropad.pixels[7] = (0,0,0)
        self.macropad.pixels[8] = (0,0,0)
        self.macropad.pixels[9] = (0,0,255)
        self.macropad.pixels[10] = (0,0,255)
        self.macropad.pixels[11] = (0,0,255)

    def get_description(self):
        return "Nav"