#Super Class for humans
class HumanBeing:

    hb = 'this is hb'
    # eyes = 2
    # ears = 2
    # legs = 2

    #super constructor args*, kwargs**
    def __init__(self,memory,hair=100,eyes=2,ears=2,legs=2):
        self.eyes = eyes
        self.ears = ears
        self.legs = legs
        self.memory = memory
        self.hair = hair

    def make_sound(self):
        print('Awwww!')

class Sam(HumanBeing):
    # def __init__(self,eyes,ears,legs):
    #     self.eyes = eyes
    #     self.ears = ears
    #     self.legs = legs

    def print_sam_info(self):
        print(f'Sam has {self.eyes} eyes, {self.ears} ears and {self.legs}')

class Rohit(HumanBeing):

    def __init__(self,name,memory,hair,eyes):
        self.name = name
        super().__init__(memory,eyes,hair)
        print(f'Rohits Memory is {self.memory}')
        print(self.name)
        print(f'Rohit has {self.eyes} eyes, {self.ears} ears and {self.legs}')
        print(f'Rohit has {self.hair}')


    def make_sound(self):
        hb = 'my local hb'
        print('Rohit Sounds Oyeeeee!')
        print(f'HB---{hb}')




# sam = Sam()
# sam.print_sam_info()
# sam.make_sound()


rohit = Rohit('Rohit','200TB',3,'10000000000000')
rohit.make_sound()