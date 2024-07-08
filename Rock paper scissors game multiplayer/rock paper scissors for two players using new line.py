import random

while True:

    choices = ["rock", "paper", "scissors"]
    players = ["femi", "samuel"]
    player_1 = None
    player_2 = None

    while player_1 not in choices:
        player_1 = input(players[0] + ": rock, paper, or scissors?: ").lower()
        print('\n' * 80)

    while player_2 not in choices:
        player_2 = input(players[1] + ": rock, paper, or scissors?: ").lower()

    print(players[0] + ": " + player_1)
    print(players[1] + ": " + player_2)

    if player_1 == player_2:
        print("Tie")

    if player_1 == "rock":
        if player_2 == "scissors":
            print(players[0] + " wins")
        if player_2 == "paper":
            print(players[1] + " wins")

    elif player_1 == "paper":
        if player_2 == "rock":
            print(players[0] + " wins")
        if player_2 == "scissors":
            print(players[1] + " wins")

    elif player_1 == "scissors":
        if player_2 == "paper":
            print(players[0] + " wins")
        if player_2 == "rock":
            print(players[1] + " wins")

    play_again = input("Do you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        break

print("Byeee!")

