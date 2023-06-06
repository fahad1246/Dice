from dice import Dice

# demonstrates some methods of dice

d = Dice()
result = d.get_sum()
print(f"We rolled a {result}")
d.roll_again()
result = d.get_sum()
print(f"We rolled a {result}")

d2 = Dice()
print(d2.get_sum())
for c in range(10):
    d2.roll_again()
    print(d2.get_sum())



message = "Number of rolls: " + str(d2.get_num_rolls())
print(message)

# the following code is used for problem #3
dice_set = Dice()
print(dice_set)

ds2 = Dice()
dice_set.roll_again()

if dice_set == ds2:
    print("Lucky!")
else:
    print("Not so lucky!")

        
def roll_count(count,number):
    
    i = 1
    counted = 0
    
    while i < count:
        d.roll_again()
        sum = d.get_sum()
        if sum == number:
            counted += 1
        i += 1
    print("Total times",number, "was repeated:", counted)


roll_count(1000,6)        

    
    
