import random

class Die:

    def __init__(self, sides=6):
        self.sides = sides
    
    def roll_dice(self):
        print(random.choice(range(1, self.sides)))


six_sided = Die()
six_sided.roll_dice()

ten_sided = Die(10)
ten_sided.roll_dice()

twenty_sided = Die(20)
twenty_sided.roll_dice()