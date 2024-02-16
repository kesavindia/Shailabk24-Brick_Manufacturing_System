'''
48 Game Character Interaction:

REQUIREMENT GATHERING:

---------------------------------------
| Enter Player Name:|_______________| |
| Choose Action:    | Attack        | |
|                   | Explore       | |
|                   | Talk          | |
|                   |_______________| |
|              Submit                  |
|_____________________________________|

ANALYSIS:

Functional Analysis:
Player will provide a name and choose actions for the game character.
Empty values: "Invalid input, please enter a name and choose an action."

Technical Analysis:
Entity Name: GameCharacterInteraction
State: Data types - STRING, Error messages - STRING
Behavior: Operators - IF, ELIF, ELSE

DESIGN (Sequence Diagrams):

Mathematics:
1. Check if a player name is provided.
2. Use nested if statements to handle different interactions based on choices.

Programming Language:
State: Define a player name and action chosen by the player.

Behavior:
1. Check if a player name is provided.
2. Use nested if statements to handle different interactions based on choices.

'''

print("Q48 GameCharacterInteraction")

# Text-based game for character interaction

# Input player name
player_name = input("Enter Player Name: ")

# Check if player name is provided
if player_name:
    print("Choose Action:")
    print("1. Attack")
    print("2. Explore")
    print("3. Talk")

    # Select action
    action_choice = input()

    if action_choice == "1":  # Attack
        print("You chose to attack. Prepare for battle!")
    elif action_choice == "2":  # Explore
        print("You chose to explore. Uncover the mysteries of the game world.")
    elif action_choice == "3":  # Talk
        print("You chose to talk. Engage in conversations with other characters.")
    else:
        print("Invalid action choice.")
else:
    print("Invalid input, please enter a name.")
