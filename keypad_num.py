from input_buffer import InputBuffer

class NumPad:
    macropad = None
    key_history = InputBuffer()

    def __init__(self, macropad):
        self.macropad = macropad

    def process_key_input(self, key_number, is_pressed):
        self.parse_key_code(key_number)
        self.key_history.push(key_number)


    def parse_key_code(self, key_number):
        if key_number == 0: self.macropad.keyboard.send(self.macropad.Keycode.ENTER)
        
        elif key_number == 1: self.macropad.keyboard.send(self.macropad.Keycode.SEVEN)
        elif key_number == 2: self.macropad.keyboard.send(self.macropad.Keycode.EIGHT)
        elif key_number == 3: self.macropad.keyboard.send(self.macropad.Keycode.NINE)
        
        elif key_number == 4: self.macropad.keyboard.send(self.macropad.Keycode.PERIOD)
        
        elif key_number == 5: self.macropad.keyboard.send(self.macropad.Keycode.FOUR)
        elif key_number == 6: self.macropad.keyboard.send(self.macropad.Keycode.FIVE)
        elif key_number == 7: self.macropad.keyboard.send(self.macropad.Keycode.SIX)
        
        elif key_number == 8: self.macropad.keyboard.send(self.macropad.Keycode.ZERO)
        
        elif key_number == 9: self.macropad.keyboard.send(self.macropad.Keycode.ONE)
        elif key_number == 10: self.macropad.keyboard.send(self.macropad.Keycode.TWO)
        elif key_number == 11: self.macropad.keyboard.send(self.macropad.Keycode.THREE)
        

    def process_encoder_input(self, position, last_position):
        print("postion: " + str(position) + ". last: " + str(last_position))
        if position is not None and last_position is not None and position < last_position:
            self.macropad.keyboard.send(self.macropad.Keycode.BACKSPACE)
            self.key_history.back()
        if position is not None and last_position is not None and position > last_position:
            print("forward")
            key = self.key_history.forward()
            if key != -1:
                self.parse_key_code(key)


    def clear_history(self):
        self.key_history.clear()


    def color_keypad(self):
        self.macropad.pixels.brightness = 0.3
        self.macropad.pixels.fill((0,0,126))


    def get_description(self):
        return "NumberPad"