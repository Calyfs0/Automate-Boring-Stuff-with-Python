import random, sys

print("ROCK, PAPER, SCISSOR")
wins = 0
losses = 0
ties = 0

while True:
    print(f"{wins} wins, {losses} losses, {ties} ties")
    print("Enter your move: (r)ock, (p)aper, (s)cissor or (q)uit")
    player_move = input()

    if player_move == "q":
        sys.exit()
    else:
        if player_move == "r":
            print("Player plays ROCK!")
        elif player_move == "p":
            print("Player plays PAPER!")
        else:
            print("Player plays SCISSOR!")
        c_move = random.randint(1, 3)
        if c_move == 1:
            print("Computer plays ROCK!")
            computer_move = "r"
        elif c_move == 2:
            print("Computer plays PAPER!")
            computer_move = "p"
        else:
            print("Computer plays SCISSOR!")
            computer_move = "s"

    if player_move == computer_move:
        print("it's a tie")
        ties = ties + 1
    elif player_move == "r" and computer_move == "p":
        print("computer wins")
        losses = losses + 1
    elif player_move == "r" and computer_move == "s":
        print("Player wins")
        wins = wins + 1
    elif player_move == "p" and computer_move == "r":
        print("Player wins")
        wins = wins + 1
    elif player_move == "p" and computer_move == "s":
        print("Computer wins")
        losses = losses + 1
    elif player_move == "s" and computer_move == "r":
        print("Computer wins")
        losses = losses + 1
    else:
        print("Player wins")
        wins = wins + 1
