""" import module functions (Python 3.xx) """
import random
import tkinter as tk # import all tkinter functions

'''
""" prepare application window """
window = tk.Tk() # create main window of application
window.title("Tkinter Hello World") # define Window title
width, height = "400", "50" # define window size in pixels
window.geometry(width + "x" + height) # set window size

""" prepare a GUI Label widget """
label_welcome = tk.Label(window, text="Hello GUI World!") # define label
label_welcome.grid() # apply label with grid method

""" execute GUI application """
window.mainloop() # launch GUI and run until user closes the window
'''

root = tk.Tk()
root.geometry('600x600')
root.title('Roll Dice')

label = tk.Label(root, text='', font=('Helvetica', 260))

def roll_dice():
    dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685', '\u27a4'] # https://www.htmlsymbols.xyz/games-symbols/dice
#    label.configure(text=f'{random.choice(dice)} {random.choice(dice)}')
    label.configure(text=dice[5])
    label.pack()

roll_dice()
button = tk.Button(root, text='roll dice', foreground='blue', command=roll_dice)
button.pack()
root.mainloop()
