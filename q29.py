# Name- ANURADHA KUMARI
# Reg no.- 23117107002
# Biomedical and Robotics Engineering

def sticks_game():
    sticks = 16
    current_player = 1  

    print(" Welcome to the Sticks Game!")
    print("There are 16 sticks. Each player can pick 1, 2, or 3 sticks on their turn.")
    print("The player who picks the LAST stick LOSES!\n")

    while sticks > 0:
        print(f"\nSticks remaining: {sticks}")
        try:
            pick = int(input(f"Player {current_player}, pick 1, 2, or 3 sticks: "))
            if pick not in [1, 2, 3]:
                print("Invalid input. You can only pick 1, 2, or 3 sticks.")
                continue
            if pick > sticks:
                print(f" Only {sticks} sticks left. You can't pick {pick}.")
                continue
        except ValueError:
            print(" Invalid input. Please enter a number.")
            continue

        sticks -= pick

        if sticks == 0:
            print(f"\nPlayer {current_player} picked the last stick and LOSES! ")
            print(f"Player {3 - current_player} wins!")
            break

       
        current_player = 2 if current_player == 1 else 1


sticks_game()