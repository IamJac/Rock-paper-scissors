from time import sleep
from subprocess import run
from game_play import play_game
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print("                               ROCK PAPER SCISSORS")
sleep(3)
run("cls",shell=True)
print(" ")
while True:
    play_game()
    repeat=str(input("Play again\nyes/No\n")).lower()
    if repeat=="no":
        print("QUITTING FROM THE GAME")
        break
    else:
        run("cls",shell=True)
        print(" ")
        print("                               ROCK PAPER SCISSORS")
        continue