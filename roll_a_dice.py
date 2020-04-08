import random


class Dice:
    def roll(self):
        #first = random.randint(1,6)
        #second = random.randint(1, 6)
        #return first,second
        dices =(1,2,3,4,5,6)
        x= random.choice(dices)
        y= random.choice(dices)
        return x,y


dice= Dice()
print(dice.roll())

#dices =(1,2,3,4,5,6).
#x= random.choice(dices)
#y= random.choice(dices)
#return x,y
