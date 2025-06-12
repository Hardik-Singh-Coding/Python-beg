import random

def get_choices():
    options = ["rock", "paper", "scissors"]
    # player_choice = "rock"
    player_choice = input("Enter a choice(rock, paper, scissors): ")

    # computer_choice = "paper"
    computer_choice = random.choice(options)

    choices = {"player": player_choice, "computer": computer_choice} # Dictionary

    return choices


def check_win(player, computer):
    print(f"You chose {player} and computer chose {computer}")
    if player == computer:
        return "It's a tie!"
    # elif player == "rock" and computer == "scissors":
    #     return "You win!"
    # elif player == "rock" and computer == "paper":
    #     return "You lose"
    # elif player == "paper" and computer == "scissors":
    #     return "You lose"
    # elif player == "paper" and computer == "rock":
    #     return "You win!"
    # elif player == "scissors" and computer == "rock":
    #     return "You lose"
    # else:
    #     return "You win"

    elif player == "rock":
        if computer == "paper":
            return "You lose"
        else:
            return "You win!"
    elif player == "paper":
        if computer == "scissors":
            return "You lose"
        else:
            return "You win!"
    elif player == "scissors":
        if computer == "rock":
            return "You lose"
        else:
            return "You win!"
    
choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)