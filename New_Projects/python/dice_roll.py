import random
import tkinter

root = tkinter.Tk()

root.geometry("700x600")
root.title("Dice Rolling Game".center(100))

label = tkinter.Label(root, font=("san-serif", 230))

#Function for dice roll
def roll():
    num_list = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    label.config(text=(random.choice(num_list) + random.choice(num_list)))
    label.pack()

button = tkinter.Button(root, text="Roll the Dice", command=roll, font=("san-serif", 20))
button.place(x = 255, y = 10)

root.mainloop()