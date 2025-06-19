import random
import tkinter as tk
from playsound import playsound

#Defined Functions
def display_score(sc):
    score.config(text=sc)
    score.pack()


def calc_score(list):
    #Check for score
    score = "YOU GOT A "
    if ('\u2685' in list):
        score += "SHIP ,"
        list.remove('\u2685')
        if ('\u2684' in list):
            score += "CAPTAIN ,"
            list.remove('\u2684')
            if ('\u2683' in list):
                score += "CREW ,"
                list.remove('\u2683')
    score += "CARGO OF "

    #Cargo Calculation
    cargo = 0
    for i in list:
        match i:
            case '\u2680':
                cargo += 1
            case '\u2681':
                cargo += 2
            case '\u2682':
                cargo += 3
            case '\u2683':
                cargo += 4
            case '\u2684':
                cargo += 5
            case '\u2685':
                cargo += 6
    
    score += str(cargo)
    #Displaying the score
    display_score(score)


def dice_display():
    r1 = roll_dice()
    r2 = roll_dice()
    r3 = roll_dice()
    r4 = roll_dice()
    r5 = roll_dice()
    list = [r1, r2, r3, r4, r5]
    dice.config(text=list)
    dice.pack()
    play()
    #Check for score
    calc_score(list)


def play():    
    playsound("Mini_Projects\python\Effects\dice_rolls.mp3", block=True)


def roll_dice():
    dice_num = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    return random.choice(dice_num)


#Main Program
root = tk.Tk()

root.attributes("-fullscreen", True)
root.title("Ship, Captain, Crew Game")

#Label for game title
title = tk.Label(root, text="SHIP, CAPTAIN, CREW!", font=("Roman", 60)).pack()

#Button to roll the dice
roll = tk.Button(root, text="ROLL THE DICE", font=("san-serif", 25), command=dice_display)
roll.place(x = 640, y = 400)

#Label for dice roll
dice = tk.Label(root, font=("san-serif", 120))

score = tk.Label(root, font=("san-serif", 40))

#Exit Button
exit = tk.Button(root, text="EXIT", font=("san-serif", 20), command=lambda:quit())
exit.place(x = 730, y = 750)

root.mainloop()