from tkinter import *
import tkinter as tk
import random

counter = 1
matchCount = 0
totalSec = 60

def main_function():

    def getusercount():
        e.pack()
        e.focus_set()
        submit.pack()

    def count():
        global counter
        counter += 1
        if counter == totalSec:
            label.destroy()
            getusercount()
            return

        fg = random.randint(0, 7)
        txt = random.randint(0, 7)
        global matchCount
        if fg == txt:
            matchCount += 1
        label.config(fg=str(colours[fg]), text=str(colours[txt]))
        label.after(1250, count)
    count()

def calculate_result():
    global matchCount
    if int(matchCount) == int(e.get()):
        txt = 'You won!!'
    else:
        txt = 'You lost, System count was {}, Your count was {}'.format(matchCount, e.get())
    submit.destroy()
    tk.Label(window, text=txt).pack()

colours = ['Red', 'Blue', 'Orange', 'Purple', 'Brown', 'Green', 'Pink', 'Black']
window = Tk()
instructions = """1)This game run's for 60 seconds.
2)If color of the text and text is same make count.
3)After 21 seconds type your total count and press submit.
4)If your count match with system code, your won or sorry try again."""

Label(window, text=instructions).pack()
window.title("Match color")
window.geometry('380x170+480+0')
window.iconbitmap('color.ico')
label = Label(window, fg="blue")
label.pack()
e = Entry(window, width=50, justify=tk.CENTER)
startButton = Button(window, text='Start', width=25, command=main_function)
startButton.pack()
submit = Button(window, text='Submit', width=25, command=calculate_result)
submit.pack()
button = Button(window, text='Quit', width=25, command=window.destroy)
button.pack()

window.mainloop()
