class DebuggerKeyPad:
    macropad = None
    display = None
    
    def __init__(self, macropad, display):
        self.macropad = macropad
        self.display = display


    def process_key_input(self, key_number, is_pressed):
        self.parse_key_code(key_number)


    def parse_key_code(self, key_number):
        if key_number == 0: 
            self.macropad.keyboard.press(
                self.macropad.Keycode.SHIFT,
                self.macropad.Keycode.F5)
            self.macropad.keyboard.release_all()
            self.display.write_line(2, "Stop")
    
        elif key_number == 1: 
            self.macropad.keyboard.send(self.macropad.Keycode.F9)
            self.display.write_line(2, "Break")
          
        elif key_number == 2: 
            self.macropad.keyboard.send(self.macropad.Keycode.F5)
            self.display.write_line(2, "Run")
                    
        elif key_number == 3: 
            self.macropad.keyboard.press(
                self.macropad.Keycode.ALT,
                self.macropad.Keycode.F5)
            self.macropad.keyboard.release_all()
            self.display.write_line(2, "Start")
     
        elif key_number == 5: 
            self.macropad.keyboard.press(
                self.macropad.Keycode.SHIFT, 
                self.macropad.Keycode.F11)
            self.macropad.keyboard.release_all()
            self.display.write_line(2, "Step Out")
              
        elif key_number == 6: 
            self.macropad.keyboard.send(self.macropad.Keycode.F10)
            self.display.write_line(2, "Step Over")
          
        elif key_number == 7: 
            self.macropad.keyboard.send(self.macropad.Keycode.F11)
            self.display.write_line(2, "Step In")
        
        elif key_number == 8: 
            self.macropad.keyboard.press(
                self.macropad.Keycode.CONTROL,
                self.macropad.Keycode.SHIFT,
                self.macropad.Keycode.B)
            self.macropad.keyboard.release_all()
            self.display.write_line(2, "Build")
        

    def process_encoder_input(self, position, last_position):
        pass


    def color_keypad(self):
        self.macropad.pixels.brightness = 0.5
        self.macropad.pixels[0] = (255,0,0)
        self.macropad.pixels[1] = (255,60,0)
        self.macropad.pixels[2] = (0,50,0)
        self.macropad.pixels[3] = (0,0,0)
        self.macropad.pixels[4] = (0,0,0)
        self.macropad.pixels[5] = (126,0,126)
        self.macropad.pixels[6] = (126,126,0)
        self.macropad.pixels[7] = (126,0,126)
        self.macropad.pixels[8] = (0,0,50)
        self.macropad.pixels[9] = (0,0,0)
        self.macropad.pixels[10] = (0,0,0)
        self.macropad.pixels[11] = (0,0,0)

    def get_description(self):
        return "Debugger"