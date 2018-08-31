import random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-V", "--version", help="show program version", action="store_true")


parser.add_argument("--sides", "-s", help="number of sides on the dice")

args = parser.parse_args()




if args.version:
	print("Dice Rolling Simulator 3.0")


try:
	if args.sides:
		q = "y"
		while q != 'n':
			if q == 'y':
				print (random.randint(1,int(args.sides)))
				q = input("Roll again? y/n ")
			else:
				q = input("Invalid response. y/n?")
	else:
		#if no sides argument set
		q = "y"
		sides = int(input("Number of sides... "))
		while q != 'n':
			
			if q == 'y':
				
				print (random.randint(1,sides))
				q = input("Roll again? y/n ")
			else:
				q = input("Invalid response. y/n?")
except ValueError:
	exit("That wasn't a number. Try Again.")

else:
	print("Thanks for playing!")
	exit()


			
print("Thanks for playing!")