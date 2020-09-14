""" import module functions (Python 3.xx) """
import tkinter as tk # import all tkinter functions

""" prepare application window """
window = tk.Tk() # create main window of application
window.title(__file__) # use this script file name as title
width, height = "400", "50" # define window size in pixels
window.geometry(width + "x" + height) # set window size

""" prepare a GUI Lable widget """
label_welcome = tk.Label(window, text="Hello GUI World!") # define label
label_welcome.grid() # apply label with grid method

""" execute GUI application """
window.mainloop() # launch GUI and run until user closes the window