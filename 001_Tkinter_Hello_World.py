""" Import module functions (Python 3.xx) """
import tkinter as tk  # Import all tkinter functions

""" Prepare application window """
window = tk.Tk()  # Create main window of application
window.title("Tkinter Hello World")  # Define Window title
width_x_height = "400x50"  # Define window size in pixels
window.geometry(width_x_height)  # Set window size

""" Prepare a GUI Label widget """
label_hello = tk.Label(window, text="Hello GUI World!") # Define text label
label_hello.grid()  # Apply label with grid method

""" Execute GUI application """
window.mainloop()  # Launch GUI and run until user closes the window
