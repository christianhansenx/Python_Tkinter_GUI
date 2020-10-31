""" import module functions (Python 3.xx) """
import tkinter as tk # import all tkinter functions

'''
""" prepare application window """
window = tk.Tk() # create main window of application
window.title("Tkinter Count Down Timer") # define Window title
width, height = "400", "50" # define window size in pixels
window.geometry(width + "x" + height) # set window size

""" prepare a GUI Label widget """
label_welcome = tk.Label(window, text="Hello GUI World!") # define label
label_welcome.grid() # apply label with grid method

""" execute GUI application """
window.mainloop() # launch GUI and run until user close the window
'''

class ExampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.label = tk.Label(self, text="", width=10)
        self.label.pack()
        self.remaining = 0
        self.countdown(10)

    def countdown(self, remaining = None):
        if remaining is not None:
            self.remaining = remaining

        if self.remaining <= 0:
            self.label.configure(text="time's up!")
        else:
            self.label.configure(text="%d" % self.remaining)
            self.remaining = self.remaining - 1
            self.after(1000, self.countdown)

if __name__ == "__main__":
    app = ExampleApp()
    app.mainloop()