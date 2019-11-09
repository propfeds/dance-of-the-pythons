from random import randint

class Die:
    def __init__(self, dice=1, sides=20, mod=0):
        self.dice=dice
        self.sides=sides
        self.mod=mod

    def roll(self):
        result=self.mod
        for _ in range(self.dice):
            result+=randint(1, self.sides)
        return result

    @property
    def roll_min(self):
        return self.dice+self.mod

    @property
    def roll_max(self):
        return self.dice*self.sides+self.mod

    @property
    def roll_average(self):
        return ((float(self.roll_min)+float(self.roll_max))/2.0)

    def __str__(self):
        die_format=''
        if self.dice!=1:
            die_format+=str(self.dice)
        die_format+='d{0}'.format(self.sides)
        if self.mod!=0:
            if self.mod>0:
                die_format+='+'
            die_format+=str(self.mod)
        return die_format