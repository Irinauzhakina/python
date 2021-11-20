class Paint:
    def __init__ (self, name):
        self.name = name

    def draw (self):
        print ('please draw')


class Pen (Paint):
    def draw (self):
        print (f'please draw{self.name}')
