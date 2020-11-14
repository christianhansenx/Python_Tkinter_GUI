""" import modules (the script is written for Python 3.xx) """
import random
import time
from timeit import default_timer as timer
import threading
import queue
import tkinter as tk # Import all tkinter functions
import tkinter.font as tkfont
import sys
import os

DICE_AMOUNT_MAX = 4 # Maximum numbers of dices the user can select
DICE_ROLLING_INTERVAL = 0.8 # The time between dice rollings in seconds

# Interval between rolling info is updated in GUI
# Must be shorter than DICE_ROLLING_INTERVAL avoid GUI update gets behind
GUI_ROLLING_UPDATE_INTERVAL = DICE_ROLLING_INTERVAL / 5

# html symbols of dice 1 to 6 eyes (https://www.htmlsymbols.xyz/games-symbols/dice)
DICE_SYMBOLS = [" ", "\u2680", "\u2681", "\u2682", "\u2683", "\u2684", "\u2685"]

STATISTICS_HEADERS = ["Dice Sum", "Occurrence", "Distribution [%]"] # table row titles

class DiceGui(tk.Tk):
    """
    All GUI visualisation and interaction is handled in this class.
    It is a inheritance of tkinter to wrap all GUI in it's own class
    """

    # Static values for styling GUI widgets
    FONT_SIZE_DEFAULT = 10
    FONT_SIZE_LARGE = int(1.4 * FONT_SIZE_DEFAULT)
    FONT_SIZE_DICE = int(12 * FONT_SIZE_DEFAULT)
    STATISTICS_COLUMN_WIDTH = 4
    STATISTICS_HEADER_BG = "light yellow"
    STATISTICS_ACTIVE_BG = "white"
    BUTTON_START_BG = "light green"
    BUTTON_STOP_BG = "pink"
    DISABLED_BG = "light gray"
    PADDING_DEFAULT = 8

    def __init__(self, script_path, script_name, data_to_gui, data_from_gui):
        self.data_to_gui = data_to_gui
        self.data_from_gui = data_from_gui
        tk.Tk.__init__(self)
        self.iconbitmap(script_path + "\\" + script_name + ".ico") # https://findicons.com/icon/download/80730/dice/48/ico
        self.title("Dice Rolling Simulator")
        self.resizable(width=False, height=False)

        # set fonts (https://www.tutorialspoint.com/python/tk_fonts.htm)
        self.default_font = tkfont.Font(size=self.FONT_SIZE_DEFAULT)
        self.large_font = tkfont.Font(size=self.FONT_SIZE_LARGE)

        self.stringvar_dice = self._dice_frame()
        self._statistics_frame()
        self._statistics_reset(0)
        self._user_input_frame()
        self._dice_rolling_update()
        self.mainloop()

    def _dice_rolling_update(self):
        interval_timer_start = timer()
        if not self.data_to_gui.empty(): # if data to gui arrived
            output_data = data_to_gui.get_nowait()
            self._dice_update(output_data["Dices"])
            self._statistics_update(output_data)
        remaining_interval = GUI_ROLLING_UPDATE_INTERVAL - (timer() - interval_timer_start)
        remaining_interval_ms = int(remaining_interval*1000)
        if remaining_interval_ms < 50:
            remaining_interval_ms = 50 # ensure minimum 50ms to update GUI
        self.after(remaining_interval_ms, self._dice_rolling_update)

    def _dice_frame(self, title="Latest Dice Roll"):
        frame = tk.LabelFrame(self, text=" "+title+" ", font=self.large_font, labelanchor="n")
        frame.grid(padx=self.PADDING_DEFAULT, pady=self.PADDING_DEFAULT, sticky="EW")
        stringvar = tk.StringVar()
        font = tkfont.Font(size=self.FONT_SIZE_DICE)
        label = tk.Label(frame, textvariable=stringvar, fg="blue", font=font)
        label.grid()
        frame.columnconfigure(0, weight=1)
        return stringvar

    def _dice_update(self, dices):
        dice_value_text = ""
        for dice_value in dices:
            dice_value_text += DICE_SYMBOLS[dice_value]
        self.stringvar_dice.set(dice_value_text)

    def _statistics_frame(self, title="Statistics"):
        statistics_frame = tk.LabelFrame(self, text=" " + title + " ", font=self.large_font, labelanchor="n")
        statistics_frame.grid(padx=self.PADDING_DEFAULT, pady=(0, self.PADDING_DEFAULT))
        self._statistics_rolling_info(statistics_frame)
        table_frame = tk.Frame(statistics_frame)
        table_frame.grid(padx=self.PADDING_DEFAULT * 2, pady=(self.PADDING_DEFAULT, self.PADDING_DEFAULT * 2))
        self._statistics_table(table_frame)

    def _statistics_table(self, frame):
        self.stat_labels = {}
        self.stat_stringvars = {}
        for column in range (0, 6*DICE_AMOUNT_MAX+1):
            column_frame = tk.Frame(frame)
            column_frame.grid(column=column, row=0)
            for row, row_header in enumerate(STATISTICS_HEADERS, 0):
                cell = tk.Frame(column_frame, relief=tk.RIDGE, borderwidth=1)
                cell.grid(column=column, row=row, sticky="EW")
                label = tk.Label(cell, font=self.default_font)
                if column == 0 or row == 0:
                    cell["bg"] = self.STATISTICS_HEADER_BG
                    label["bg"] = self.STATISTICS_HEADER_BG
                    if column == 0:
                        label["text"] = row_header
                        alignment = "W"
                        if row > 0: # new statistics row containing values
                            self.stat_labels[row_header] = []
                            self.stat_stringvars[row_header] = []
                    else: # row 0
                        label["text"] = str(column)
                        label["width"] = self.STATISTICS_COLUMN_WIDTH
                        alignment = "EW"
                else: # statistics cell containing value
                    stringvar = tk.StringVar()
                    label["textvariable"] = stringvar
                    self.stat_labels[row_header].append(label)
                    self.stat_stringvars[row_header].append(stringvar)
                    alignment = "E"
                label.grid(column=column, row=row, sticky=alignment)
                cell.columnconfigure(0, weight=1)

    def _statistics_rolling_info(self, frame):
        self.stringvar_rolling_counts = tk.StringVar()
        roll_count_frame = tk.Frame(frame)
        roll_count_frame.grid(padx=self.PADDING_DEFAULT*2, pady=self.PADDING_DEFAULT, sticky="EW")
        cell = tk.Frame(roll_count_frame, relief=tk.RIDGE, borderwidth=1)
        cell.grid()
        label = tk.Label(cell, text="Rollings", font=self.default_font)
        label["bg"] = self.STATISTICS_HEADER_BG
        label.grid()
        cell = tk.Frame(roll_count_frame, relief=tk.RIDGE, borderwidth=1)
        cell.grid(row=0, column=1)
        label = tk.Label(cell, textvariable=self.stringvar_rolling_counts, font=self.default_font, anchor='e')
        label["bg"] = self.STATISTICS_ACTIVE_BG
        label.grid(ipadx=int(self.FONT_SIZE_DEFAULT/3), sticky="E") # ipadx to create a little space in front of value

    def _statistics_reset(self, number_of_dices):
        self.stringvar_rolling_counts.set("0")
        self._dice_update([])
        first_active_column = number_of_dices - 1
        last_active_column = number_of_dices * 6 - 1
        for row, row_header in enumerate(self.stat_labels, 0):
            label_list = self.stat_labels[row_header]
            stringvar_list = self.stat_stringvars[row_header]
            for column in range(0, 6 * DICE_AMOUNT_MAX):
                label = label_list[column]
                stringvar_list[column].set("")
                if column < first_active_column or column > last_active_column:
                    label["bg"] = self.DISABLED_BG
                    label.master["bg"] = self.DISABLED_BG
                else:
                    label["bg"] = self.STATISTICS_ACTIVE_BG
                    label.master["bg"] = self.STATISTICS_ACTIVE_BG

    def _statistics_update(self, data):
        self.stringvar_rolling_counts.set(data["Rollings"])
        first_active_column = self.dice_amount_int.get() - 1
        last_active_column = self.dice_amount_int.get() * 6 - 1
        for index in range(first_active_column, last_active_column+1):
            self.stat_stringvars["Occurrence"][index].set(data["Occurrence"][index])
            self.stat_stringvars["Distribution [%]"][index].set(data["Distribution [%]"][index])

    def _user_input_frame(self):
        input_frame = tk.Frame()
        input_frame.grid(pady=(0, self.PADDING_DEFAULT))

        self.button_start = tk.Button(input_frame, text="Start", font=self.large_font, command=self._start_dice_rolling)
        self.button_start = tk.Button(input_frame, text="Start", font=self.large_font, command=self._start_dice_rolling)
        self.button_start.grid()

        self.button_stop = tk.Button(input_frame, text="Stop", font=self.large_font, command=self._stop_dice_rolling)
        self.button_stop.grid(row=0, column=1, padx=(self.PADDING_DEFAULT, 0))

        self.label_dices = tk.Label(input_frame, text="Number of dices", font=self.large_font)
        self.label_dices.grid(row=0, column=3, padx=(self.PADDING_DEFAULT*5, 0))
        self.dice_amount_int = tk.IntVar()
        self.dice_amount_int.set(1)
        self.spinbox_dices = tk.Spinbox(input_frame, from_=1, to=DICE_AMOUNT_MAX, font=self.large_font, justify="right")
        self.spinbox_dices["textvariable"] = self.dice_amount_int
        self.spinbox_dices["width"] = 2
        self.spinbox_dices.grid(row=0, column=4, padx=(int(self.PADDING_DEFAULT/2), 0))
        self.spinbox_dices["readonlybackground"] = self.spinbox_dices["bg"]
        self.spinbox_dices["selectbackground"] = self.spinbox_dices["bg"] # because of readonly then no select highlight
        self.spinbox_dices["selectforeground"] = self.spinbox_dices["fg"] # because of readonly then no select highlight

        self._stop_dice_rolling(only_widgets=True)

    def _start_dice_rolling(self):
        self.button_start["state"] = "disabled"
        self.button_start["bg"] = self.DISABLED_BG
        self.spinbox_dices["state"] = "disabled"
        self.button_stop["state"] = "normal"
        self.button_stop["bg"] = self.BUTTON_STOP_BG
        self._statistics_reset(self.dice_amount_int.get())
        data_packet = DataFromGui()
        data_packet.start_dice_rolling(self.dice_amount_int.get())
        self.data_from_gui.put(data_packet)

    def _stop_dice_rolling(self, only_widgets=False):
        self.button_stop["state"] = "disabled"
        self.button_stop["bg"] = self.DISABLED_BG
        self.button_start["bg"] = self.BUTTON_START_BG
        self.button_start["state"] = "normal"
        self.spinbox_dices["state"] = "readonly"
        if not only_widgets:
            data_packet = DataFromGui()
            data_packet.stop_dice_rolling()
            self.data_from_gui.put(data_packet)


class DiceRolling():
    """
    This is the "dice rolling generator" thread which simulate the dice rollings.
    It's running asynchronous to the GUI updates.
    Thread safe data queues are used for interchange data between "dice rolling generator" and GUI.
    """

    def __init__(self, data_to_gui, data_from_gui):
        thread_target = self._rolling_generator_thread
        thread_name = __class__.__name__ + "." + thread_target.__name__
        rolling_thread = threading.Thread(target=thread_target, name=thread_name, args=(data_from_gui, data_to_gui,))
        rolling_thread.setDaemon(True) # stop thread when script exits
        rolling_thread.start()

    def _rolling_generator_thread(self, data_from_gui, data_to_gui):
        NUMBER_OF_RESULTS = DICE_AMOUNT_MAX * 6
        dices = [0] * DICE_AMOUNT_MAX
        statistics_counts = [0] * NUMBER_OF_RESULTS
        statistics_distribution = [0] * NUMBER_OF_RESULTS
        dice_rolling = False
        while True: # loop until the script is terminated (by user)
            if not data_from_gui.empty(): # if data from gui arrived
                input_data = data_from_gui.get_nowait()
                if input_data["Command"] == "START":
                    dice_rolling = True
                    number_of_dices = input_data["Dice Amount"]
                    print("== Dice Rolling Session Started with %i dice(s) ==" % number_of_dices)
                    rolling_count = 0
                    for index in range(0, NUMBER_OF_RESULTS):
                        statistics_counts[index] = 0
                        statistics_distribution[index] = 0
                    roll_interval_timer_start = timer() - DICE_ROLLING_INTERVAL # to trig first roll immediately
                if input_data["Command"] == "STOP":
                    print("== Dice Rolling Session Stopped ==\n")
                    dice_rolling = False
            if dice_rolling and timer() - roll_interval_timer_start >= DICE_ROLLING_INTERVAL:
                roll_interval_timer_start = timer()
                rolling_count += 1
                self._dice_roll(rolling_count, number_of_dices, dices)
                data_packet = DataToGui(rolling_count, number_of_dices, dices)
                data_packet.statistics(statistics_counts, statistics_distribution)
                data_to_gui.put(data_packet)
            time.sleep(0.1)

    @staticmethod # is static due to it's a supporting function to a thread in the same class
    def _dice_roll(rolling_count, number_of_dices, dices):
        for dice_index in range(0, number_of_dices):
            dice = random.randint(1, 6)
            dices[dice_index] = dice
        print_line = "    Dice Roll " + str(rolling_count) + " = "
        for dice_index in range(0, number_of_dices):
            dice = dices[dice_index]
            if dice_index > 0:
                print_line += ", "
            print_line += str(dice)
        print(print_line)


class DataFromGui():
    """
    Data packet class for wrapping data to be transferred from GUI to "dice rolling generator".
    The data are signals to start and stop the "dice rolling generator"
    """

    def start_dice_rolling(self, number_of_dices):
        self.data = {"Command":"START", "Dice Amount":number_of_dices}

    def stop_dice_rolling(self):
        self.data = {"Command":"STOP"}

    def __getitem__(self, key):
        return self.data[key]


class DataToGui():
    """
    Data packet class for wrapping data to be transferred from "dice rolling generator" to GUI.
    The data packet contain values of dice rolling and statistics in formats to easily be visualised by GUI.
    """

    def __init__(self, rolling_count, number_of_dices, dices):
        self.data = {}
        self.rolling_count = rolling_count
        self.number_of_dices = number_of_dices
        self.data["Rollings"] = str(rolling_count)
        self.data["Dices"] = [0] * number_of_dices
        for dice_index in range(0, self.number_of_dices):
            self.data["Dices"][dice_index] = dices[dice_index]

    def statistics(self, statistics_counts, statistics_distribution):
        self.data["Occurrence"] = [""] * self.number_of_dices * 6
        self.data["Distribution [%]"] = [""] * self.number_of_dices * 6
        sum = 0
        for dice_index in range(0, self.number_of_dices):
            sum += self["Dices"][dice_index]
        statistics_counts[sum-1] += 1
        for sum_index in range(self.number_of_dices-1, self.number_of_dices*6):
            counts = statistics_counts[sum_index]
            statistics_distribution[sum_index] = statistics_counts[sum_index] / self.rolling_count * 100
            if counts > 0:
                self["Occurrence"][sum_index] = str(counts)
                self["Distribution [%]"][sum_index] = str("%.1f" % statistics_distribution[sum_index])

    def __getitem__(self, key):
        return self.data[key]


if __name__ == "__main__":
    SCRIPT_PATH_FILE = os.path.basename(sys.argv[0])
    SCRIPT_FILE_NAME = os.path.basename(sys.argv[0])
    SCRIPT_NAME = os.path.splitext(SCRIPT_FILE_NAME)[0]

    try:
        SCRIPT_PATH = sys._MEIPASS
    except:
        SCRIPT_PATH = os.path.dirname(sys.argv[0])

    print("=== SCRIPT: %s ====\n" % SCRIPT_NAME)

    data_to_gui = queue.Queue() # Thread safe data packets transfer to gui
    data_from_gui = queue.Queue() # Thread safe data packets transfer from gui
    rolling_generator = DiceRolling(data_to_gui, data_from_gui) # Aim "dice rolling generator"
    DiceGui(SCRIPT_PATH, SCRIPT_NAME, data_to_gui, data_from_gui) # Aim the GUI
