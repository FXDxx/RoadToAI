import random

game_turns = ['Rock', 'Paper', 'Scissors']

try:
    for i in range(0, 1000):

        player1_turn = input("Enter turn: ")  # = random.choice(game_turns)
        print("Player 1: ", player1_turn)
        player2_turn = input("Enter turn 2: ")  # = random.choice(game_turns)
        print("Player 2: ", player2_turn)


        if player1_turn == 'Rock' and player2_turn == 'Rock' and player1_turn == player2_turn:
            print("Draw..\nnext turn..")
            continue
        elif player1_turn == 'Rock' and player2_turn == 'Scissors' and player1_turn != player2_turn:
            print("Player 1 wins")
            break
        elif player1_turn == 'Rock' and player2_turn == 'Paper' and player1_turn != player2_turn:
            print("Player 2 wins")
            break
        elif player1_turn == 'Paper' and player2_turn == 'Paper' and player1_turn == player2_turn:
            print("Draw..\nnext turn..")
            continue
        elif player1_turn == 'Paper' and player2_turn == 'Scissors' and player1_turn != player2_turn:
            print("Player 2 wins")
            break
        elif player1_turn == 'Paper' and player2_turn == 'Rock' and player1_turn != player2_turn:
            print("Player 1 wins")
            break
        elif player1_turn == 'Scissors' and player2_turn == 'Scissors' and player1_turn == player2_turn:
            print("Draw..\nnext turn..")
            continue
        elif player1_turn == 'Scissors' and player2_turn == 'Rock' and player1_turn != player2_turn:
            print("Player 2 wins")
            break
        elif player1_turn == 'Scissors' and player2_turn == 'Paper' and player1_turn != player2_turn:
            print("Player 1 wins")
            break
except TypeError as e:
    e.message = 'Type not compatible'


