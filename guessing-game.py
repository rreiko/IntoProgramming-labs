answer = "shark"
guess = input
print("ANIMAL GUESSING GAME")
print("I’m thinking of a sea animal")

while not guess == answer:
    guess = input("Enter an animal name: ").lower()
    if guess == answer:
        print("You guessesd it!")
    else: 
        print("That's not right try again")
	
