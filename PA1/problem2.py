import random

def roll_dice():
    return random.randint(1, 6) + random.randint(1, 6)

def play_one_game():
    first_roll = roll_dice()
    if first_roll == 7 or first_roll == 11:
        print(f"You rolled {first_roll}\nYou win!!")
        return 1
    if first_roll == 2 or first_roll == 3 or first_roll == 12:
        print(f"You rolled {first_roll}\nSorry, you lose!")
        return 0
    else:
        print(f"You rolled {first_roll}\nYour point is {first_roll}\n")
        new_roll = roll_dice()
        while first_roll != new_roll:
            new_roll = roll_dice()
            print(f"You rolled {new_roll}")
            if new_roll == 7:
                print("Sorry, you lose!\n")
                return 0
        if first_roll == new_roll:
            print("You win!!\n")
            return 1

def craps():
    dashed_line = "-" * 28
    message = "Welcome to the Craps program"
    welcome_message = f"{dashed_line:^60}\n{message:^60}\n{dashed_line:^60}\n"
    print(welcome_message)

    initial_balance = 1000

    print(f"Your initial bank balance is ${initial_balance}.")

    while initial_balance > 0:
        wager = int(input("\nWhat is your wager? "))

        while wager > initial_balance:
            wager = int(input(f"Cannot wager more than ${wager}. Re-enter wager: "))

        print("Okay, let's play.\n")

        results = play_one_game()

        if results == 1:
            initial_balance += wager
            print(f"Your new bank balance is ${initial_balance}\n")

        if results == 0:
            initial_balance -= wager
            print(f"Your new bank balance is ${initial_balance}\n")

        if initial_balance == 0:
            print("Sorry, you're broke!")
            break

        play_again = input("Do you want to play again? [y/n] ")

        if play_again == "y":
            continue

        if play_again == "n":
            break

    if initial_balance > 1000:
        print("\nYou gained money. Good job!")

    if initial_balance < 1000 and initial_balance != 0:
        print("\nSorry you lost money. Better luck next time!")

craps()