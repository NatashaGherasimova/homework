my_number = 3
number_to_guess = 10
while my_number != number_to_guess:
    my_number = int(input("Enter your number: "))
    if my_number < number_to_guess:
        print("The number is bigger")
    else my_number > number_to_guess:
        print("The number is smaller")
print("Game over!")
