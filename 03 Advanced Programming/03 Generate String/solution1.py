def generate_string(string, frequency):
    n = 0
    while n < len(string):
        result = string[n] * frequency
        yield result
        n += 1


class GenerateString:
    def __init__(self, string, frequency):
        self.string = string
        self.frequency = frequency

    def __iter__(self):
        self.frequency_count = 0
        self.index = 0
        return self
        
    def __next__(self):
        if self.frequency_count >= self.frequency:
            self.frequency_count = 0
            self.index += 1
            
        if self.index >= len(self.string):
            raise StopIteration
        
        self.frequency_count += 1
        return self.string[self.index]