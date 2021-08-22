class MacroPadDisplay:
    macropad = None
    sleep_count = 0
    sleep_threshold = 5000


    def __init__(self, macropad):
        self.macropad = macropad
        self.text_lines = macropad.display_text()
        self.macropad.pixels.brightness = 0.03

    def set_description(self, description):        
        self.write_line(0, description)


    def update_position(self, position):
        self.write_line(1, "Pos.: " + str(position))


    def update_sleep_count(self, has_input = True):
       self.sleep_count = 0 if has_input else (self.sleep_count + 1)


    def write_line(self, line, message):
        if self.sleep_count < self.sleep_threshold and self.text_lines[line].text != message:
            self.text_lines[line].text = message


    def write_to_display(self):
        if self.sleep_count > self.sleep_threshold:
            for i in range(0,3):
                self.text_lines[i].text = ""
    
        #self.write_line(5, "ZCount: "+str(self.sleep_count))
        self.text_lines.show()


    def is_sleeping(self):
        return self.sleep_count > self.sleep_threshold


    def color_keypad(self):
        self.macropad.pixels.fill((0,0,0))     


         
