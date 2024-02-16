import time
'''Design a text-based game where the player controls a character. Use nested if statements to handle
different interactions based on the player&#39;s choices, leading to multiple possible outcomes.'''
def intro():
    print("You find yourself standing at the entrance of a dark and mysterious cave.")
    print("Do you dare to enter?")

def choose_path():
    print("\nChoose your path:")
    print("1. Enter the cave.")
    print("2. Walk away.")

    choice = input("Enter your choice (1 or 2): ")
    return choice

def explore_cave():
    print("\nAs you venture into the cave, you encounter two tunnels.")
    print("Each tunnel has its own challenges and rewards.")

    print("1. Left tunnel.")
    print("2. Right tunnel.")

    choice = input("Enter your choice (1 or 2): ")
    return choice

def left_tunnel():
    print("\nYou chose the left tunnel.")
    print("A swarm of bats emerges, but you find a hidden treasure chest.")

    print("1. Fight off the bats.")
    print("2. Grab the treasure and run.")

    choice = input("Enter your choice (1 or 2): ")
    return choice

def right_tunnel():
    print("\nYou chose the right tunnel.")
    print("A mysterious light illuminates a path filled with ancient symbols.")

    print("1. Decode the symbols.")
    print("2. Ignore the symbols and continue walking.")

    choice = input("Enter your choice (1 or 2): ")
    return choice

def main():
    intro()

    # First decision point
    path_choice = choose_path()

    if path_choice == '1':
        # Second decision point
        tunnel_choice = explore_cave()

        if tunnel_choice == '1':
            # Third decision point
            left_choice = left_tunnel()

            if left_choice == '1':
                print("\nYou successfully fought off the bats and obtained the treasure!")
            else:
                print("\nYou grabbed the treasure but got bitten by the bats. You escape with minor injuries.")

        else:
            # Third decision point
            right_choice = right_tunnel()

            if right_choice == '1':
                print("\nYou successfully decoded the symbols and found a secret passage leading to a hidden exit!")
            else:
                print("\nIgnoring the symbols, you encounter a trap and narrowly escape with your life.")

    else:
        print("\nYou decide not to enter the cave. Your adventure ends here.")

if __name__ == "__main__":
    main()
