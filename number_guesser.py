import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Please type a number larger than 0 next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()

random_number = random.randint(1, top_of_range)  # Ensures valid range (1 to top_of_range)
guesses = 0
while True:
    guesses +=1
    user_guess = input("Make a guess: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        continue  # Ensures loop continues if input is invalid

    if user_guess == random_number:
        print("You got it!")
        break  # Exits loop when correct guess is made
    
    elif user_guess > random_number:  #elif is a combination of an else and a if statement, makes the code look cleaner
            print("You were above the number!")
    else:
            print("You were below the number!")

print("You got it in", guesses, "guesses") # the comma replaces the +