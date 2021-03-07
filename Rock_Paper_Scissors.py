import random
import pyfiglet
import termcolor2

TryAgain = True
while TryAgain == True:
    welcome_into = pyfiglet.figlet_format("W e l c o m e ")
    print(termcolor2.colored(welcome_into,color="green"))
    print("You can see the game guide below:\n")
    print(" * "*20, "\n")
    print(" 1. Rock \n\n 2. paper \n\n 3. Scissors \n\n")
    ComputeChoise = random.randint(1, 3)
    yourChoise = int(input("Enter your number : "))

    while yourChoise > 3:
        result = termcolor2.colored(
            "Please Enter a number between 1 and 3 ", color="red")
        print(result)
        yourChoise = int(input("Enter your number : "))
        continue

    if yourChoise == ComputeChoise:
        print("This game does not win")
    elif yourChoise == 1 and ComputeChoise == 3:
        print(
            f"Your choice is : Rock and Computer choice is : Scissors --> You get the game")
    elif yourChoise == 2 and ComputeChoise == 1:
        print(f"Your choice is : Paper and Computer choice is : Rock --> You get the game")
    elif yourChoise == 3 and ComputeChoise == 2:
        print(
            f"Your choice is : Scissors and Computer choice is : Paper --> You get the game")
    else:
        print("You lose the Game :(")
    print("Do you want to continue the game? (y oder n)")
    response = input()
    if response[0] == "y":
        TryAgain = True
    else:
        TryAgain = False
        break
print(pyfiglet.figlet_format("B y e"))
