letter_to_guess = "e"
letter = " "
while letter != letter_to_guess:
    print("Enter your letter: ")
    letter = input()
    if letter == letter_to_guess:
        print("You have guessed!")
    else:
        print ("Try again!")
print("Game over!")