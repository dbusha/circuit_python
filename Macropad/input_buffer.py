class InputBuffer:
    buffer_size = 10
    buffer = [-1] * buffer_size
    start = 1
    end = 1
    index = 1

    def __init__(self):
        pass
   
    def push(self, item):
        if self.index != self.end:
            self.end = self.index
        next_end = (self.end + 1) % self.buffer_size
        next_start = (self.start + 1) % self.buffer_size
        if next_end == self.start:
            self.start = next_start
        
        self.end = next_end
        self.index = next_end
        self.buffer[self.end] = item

    def back(self):
        self.print_debug_status("back")
        if self.index == self.start:
            return -1
        self.index = self.index - 1 if self.index > 0 else self.buffer_size -1
        return self.buffer[self.index]

    def forward(self):
        self.print_debug_status("forward")
        next_index = (self.index + 1) % self.buffer_size
        if next_index == self.start or self.index == self.end:
            return -1
       
        key = self.buffer[self.index]
        self.index = next_index
        return key
       
    def clear(self):
        self.start = 0
        self.end = 0
        self.index = 0
        self.buffer = [-1] * self.buffer_size

    def print_debug_status(self, direction):
        #print(str(direction) + " - start: "+str(self.start)+", end: " +str(self.end) +", index: " +str(self.index) )
        #print("buffer: " + ', '.join(str(i) for i in self.buffer))
        pass