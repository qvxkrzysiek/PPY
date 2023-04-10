import random
import getpass

def play_one_on_one(player1, player2, rounds):
    scores = {player1: 0, player2: 0}
    for round_num in range(1, rounds + 1):
        print(f"Round {round_num}:")
        move1 = getpass.getpass(f"{player1}, choose your move (rock/paper/scissors): ")
        move2 = getpass.getpass(f"{player2}, choose your move (rock/paper/scissors): ")
        print(f"{player1} chose: {move1}")
        print(f"{player2} chose: {move2}")
        if move1 == move2:
            print("It's a tie!")
        elif (move1 == "rock" and move2 == "scissors") or \
             (move1 == "scissors" and move2 == "paper") or \
             (move1 == "paper" and move2 == "rock"):
            print(f"{player1} wins the round!")
            scores[player1] += 1
        else:
            print(f"{player2} wins the round!")
            scores[player2] += 1
    return scores

def play_with_computer(player, rounds):
    scores = {player: 0, "Computer": 0}
    for round_num in range(1, rounds + 1):
        print(f"Round {round_num}:")
        move = getpass.getpass(f"{player}, choose your move (rock/paper/scissors): ")
        computer_move = random.choice(["rock", "paper", "scissors"])
        print(f"{player} chose: {move}")
        print(f"Computer chose: {computer_move}")
        if move == computer_move:
            print("It's a tie!")
        elif (move == "rock" and computer_move == "scissors") or \
             (move == "scissors" and computer_move == "paper") or \
             (move == "paper" and computer_move == "rock"):
            print(f"{player} wins the round!")
            scores[player] += 1
        else:
            print("Computer wins the round!")
            scores["Computer"] += 1
            
    return scores

print("Rock-Paper-Scissors Game")

try:
    num_rounds = int(input("Enter the number of rounds: "))
    if num_rounds <= 0:
        raise ValueError
except ValueError:
    print("Invalid number of rounds.")
    exit()

try:
    game_mode = input("Choose game mode (1 - one player vs computer, 2 - two players): ")
    if game_mode != "1" and game_mode != "2":
        raise ValueError
except ValueError:
    print("Invalid game mode.")
    exit()

player1_name = input("Enter player 1 name: ")

if game_mode == "1":
    scores = play_with_computer(player1_name, num_rounds)
    player2_name = "Computer"
else:
    player2_name = input("Enter player 2 name: ")
    scores = play_one_on_one(player1_name, player2_name, num_rounds)

print("Game over!")

for player, score in scores.items():
    print(f"{player}: {score}")

if scores[player1_name] > scores[player2_name]:
    print(f"{player1_name} wins!")
elif scores[player1_name] < scores[player2_name]:
    print(f"{player2_name} wins!")
else:
    print("It's a tie!")
