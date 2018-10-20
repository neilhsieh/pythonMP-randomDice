import random
import time

roll = True
diceMin = int(input("Enter a min number: "))
diceMax = int(input("Enter a max number: "))
print("A dice will now roll a random number between those two values...")

#time.sleep(1)

while(roll):
	print (random.randint(diceMin,diceMax))
	rollAgain = input("Would you like to roll again? y/n ")
	if rollAgain == 'y':
		roll = True
	else:
		roll = False