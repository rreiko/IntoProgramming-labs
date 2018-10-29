answer = "shark"
guess = input
YN = input
print("ANIMAL GUESSING GAME")
print("I’m thinking of a sea animal")

while not guess == answer:
    guess = input("Enter an animal name: ").lower()
    if guess == answer:
        print("You guessesd it!")
        YN = input("Do you like this animal? (yes or no)   ").lower()
        if YN[0] == "y":
            print("Yes, theyre fun!")
        else:
            print("I understand, they're scary.")
    elif guess[0] == "q".lower():
        break
    else: 
        print("That's not right try again")
	
