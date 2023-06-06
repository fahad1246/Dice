import random

class Dice:

    def __init__(self):
        "constructor rolls dice and sets roll count to 1"
        self.count = 1
        self.die1 = random.randint(1, 6)
        self.die2 = random.randint(1, 6)

    def roll_again(self):
        "rolls both dice and increments the roll count"
        self.count = self.count + 1
        self.die1 = random.randint(1, 6)
        self.die2 = random.randint(1, 6)

    def get_sum(self):
        "return the sum of the last roll"
        return self.die1 + self.die2

    def get_roll(self, die_number):
        if die_number == 1:
            return self.die1
        elif die_number == 2:
            return self.die2
        else:
            raise Exception("die_number must be 1 or 2")

    def get_num_rolls(self):
        "return the number of times that dice have been rolled"
        return self.count

    def __str__(self):
        "string representation that dispays both rolls"
        return str(self.die1) + " " + str(self.die2)
    
    def __equals__(self, dice2):
        "returns true if both dice have the same rolls"
        return self.die1 == dice2.die1 and self.die2 == dice2.die2
        
