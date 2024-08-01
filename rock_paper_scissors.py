import random

# Define the game options and their winning conditions
options = ["rock", "paper", "scissors"]
winning_conditions = {
    ("rock", "scissors"): "rock crushes scissors",
    ("paper", "rock"): "paper covers rock",
    ("scissors", "paper"): "scissors cuts paper"
}

user_wins = 0
computer_wins = 0

def get_computer_choice():
    return random.choice(options)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "draw"
    elif (user_choice, computer_choice) in winning_conditions:
        return "user"
    else:
        return "computer"

def print_winner_message(winner, user_choice, computer_choice):
    if winner == "draw":
        print(f"Both chose {user_choice}. It's a draw!")
    elif winner == "user":
        print(f"You won! {winning_conditions[(user_choice, computer_choice)]}.")
    else:
        print(f"You lost! {winning_conditions[(computer_choice, user_choice)]}.")

print("Welcome to Rock, Paper, Scissors!")

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    
    if user_input == "q":
        break

    if user_input not in options:
        print("Invalid choice. Please choose Rock, Paper, or Scissors.")
        continue

    computer_pick = get_computer_choice()
    print("Computer picked", computer_pick + ".")

    winner = determine_winner(user_input, computer_pick)
    
    if winner == "user":
        user_wins += 1
    elif winner == "computer":
        computer_wins += 1

    print_winner_message(winner, user_input, computer_pick)

print(f"You won {user_wins} times.")
print(f"Computer won {computer_wins} times.")
print("Goodbye!")
