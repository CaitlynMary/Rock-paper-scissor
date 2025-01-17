import random

print("************ROCK,PAPER,SCISSORS*****************")


def get_choices():
    player_choice = input("Enter a choice(rock,paper,scissors:):")
    print("---------------------------------------------")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}

    return choices


def check_win(player, computer):
    print(f"You chose {player} , computer chose {computer}.")
    if player == computer:
        return "It is a tie!!"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors and you WIN!!!"
        else:
            return "paper covers rock and you LOSE!!"

    elif player == "paper":
        if computer == "rock":
            return "paper covers rock and you WIN!!!"
        else:
            return "scissors cuts paper and you LOSE!!"

    elif player == "scissors":
        if computer == "rock":
            return "Rock smashes scissors and you LOSE!!!"
        else:
            return "scissors cuts paper and you WIN!!!!"


choices = get_choices()
result = check_win(choices["player"], choices["computer"])

print(result)
