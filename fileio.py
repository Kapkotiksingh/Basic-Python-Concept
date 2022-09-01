n = 8
number_of_guesses = 1
print("number is guesses is limited to only 9 time : ")
while  number_of_guesses <= 9:
    guess_number = int(input("Guess The Number.\n"))

    if guess_number < 18:
        print("Your enter less  number please input greater number.\n")

    if guess_number > 18:
        print("Your enter less  number please input greater number.\n")
    else:
        print("You Are Win This Game.\n")
        print(number_of_guesses, "number of guesses he took to finish. ")
        break
    print(9-number_of_guesses,"number of guesses left ")
    number_of_guesses = number_of_guesses+1

if number_of_guesses > 9:
    print("Game Over")
