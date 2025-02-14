from random import choice
class InvalidInput(Exception):
    pass


def determine_winner(user,computer):
    print(F"Your Input = {user}\nComputer's choice = {computer}")
    if user==computer:
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print("                                   IT'S A TIE")
        return
    if ((user=="rock" and computer=="scissors") or
            (user=="scissors" and computer=="paper")
            or(user=="paper" and computer=="rock")):
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print("                                   YOU WIN")
        return
    else:
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print("                                  YOU LOSE")
        return
def play_game():
    game_choices = ["rock", "paper", "scissors"]
    try:
        user_input=str(input("Input your option\nRock\nPaper\nScissors\n")).lower()
        if user_input not in game_choices:
            raise InvalidInput("Invalid input")
        else:
            computer_choice = choice(game_choices)
            determine_winner(user_input, computer_choice)
            return
    except InvalidInput as e:
        print(e)
