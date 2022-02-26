# ************************ HOMEWORK 1 QUESTION 2 **************************
def question2(player1, player2):
    ### WRITE CODE HERE
    # DETERMINES WHICH PLAYER WINS IN THE GAME "ROCK PAPER SCISSORS"
    # CHECK WHAT THE FIRST PLAYER PLAYS AND COMPARES TO WHAT THE SECONDS PLAYER PLAYS.
    # THEN PRINTS WHO WON OR IF THERE IS A TIE

    # WHEN THERE IS A TIE
    if player2 == player1:
        print("It is a tie!")

    # IF PLAYER1 PLAYS ROCK
    if player1 == "rock":
        if player2 == "paper":
            print("Player 2 won!")
        if player2 == "scissors":
            print("Player 1 won!")

    # IF PLAYER1 PLAYS PAPER
    if player1 == "paper":
        if player2 == "rock":
            print("Player 1 won!")
        if player2 == "scissors":
            print("Player 2 won!")

        # IF PLAYER1 PLAYS SCISSORS
    if player1 == "scissors":
        if player2 == "rock":
            print("Player 2 won!")
        if player2 == "paper":
            print("Player 1 won!")
