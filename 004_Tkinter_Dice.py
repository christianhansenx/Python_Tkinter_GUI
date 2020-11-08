""" import module functions (Python 3.xx) """
import random
import time
import threading
import tkinter as tk # import all tkinter functions
import tkinter.font as tkfont

STATISTICS_HEADERS = ["Dice Sum", "Result Counts", "Distribution [%]"]
DICE_AMOUNT_MAX = 5
DICE_ROLLING_INTERVAL = 3.0 # seconds

# html symbols of dice 1 to 6 eyes (https://www.htmlsymbols.xyz/games-symbols/dice)
DICE_SYMBOLS = ["", "\u2680", "\u2681", "\u2682", "\u2683", "\u2684", "\u2685"]


class DiceGui(tk.Tk): # Inheritance of tkinter to keep all GUI in it's own class

    PADDING_DEFAULT = 8
    DEFAULT_FONT_SIZE = 10
    FONT_FRAME_FACTOR = 1.4
    DICE_FONT_SIZE = 128
    STATISTICS_COLUMN_WIDTH = 4
    STATISTICS_HEADER_BG = "light yellow"
    STATISTICS_ACTIVE_BG = "white"
    STATISTICS_INACTIVE_BG = "light gray"

    def __init__(self):
        tk.Tk.__init__(self)
        self.dice_amount = DICE_AMOUNT_MAX
        self.dice_values = [6] * self.dice_amount

        # set fonts (https://www.tutorialspoint.com/python/tk_fonts.htm)
        self.default_font = tkfont.Font(size=self.DEFAULT_FONT_SIZE)
        self.frame_font = tkfont.Font(size=int(self.FONT_FRAME_FACTOR * self.DEFAULT_FONT_SIZE))

        self.stringvar_dice = self.dice_frame()
        self.dice_update()
        self.statistics_frame()
        self.statistics_reset()
        self.statistics_update(5, "8", "  1.6")
#        self.columnconfigure(0, weight=1)
        self.title("Dice Rolling Simulator")
        self.resizable(width=False, height=False)
        self.mainloop()

    def dice_frame(self, title="Latest Dice Roll"):
        frame = tk.LabelFrame(self, text=" "+title+" ", font=self.frame_font, labelanchor="n")
        frame.grid(padx=self.PADDING_DEFAULT, pady=self.PADDING_DEFAULT, sticky="EW")
        stringvar = tk.StringVar()
        font = tkfont.Font(size=self.DICE_FONT_SIZE)
        label = tk.Label(frame, textvariable=stringvar, fg="blue", font=font)
        label.grid()
        frame.columnconfigure(0, weight=1)
        return stringvar

    def dice_update(self):
        dice_value_text = ""
        for dice_value in self.dice_values:
            dice_value_text += DICE_SYMBOLS[dice_value]
        self.stringvar_dice.set(dice_value_text)

    def statistics_frame(self, title="Statistics"):
        statistics_frame = tk.LabelFrame(self, text=" " + title + " ", font=self.frame_font, labelanchor="n")
        statistics_frame.grid(padx=self.PADDING_DEFAULT, pady=(0, self.PADDING_DEFAULT))
        self.statistics_rolling_info(statistics_frame)
        table_frame = tk.Frame(statistics_frame)
        table_frame.grid(padx=self.PADDING_DEFAULT * 2, pady=(self.PADDING_DEFAULT, self.PADDING_DEFAULT * 2))
        self.statistics_table(table_frame)
#        statistics_frame.columnconfigure(0, weight=1)

    def statistics_table(self, frame):
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

    def statistics_rolling_info(self, frame):
        self.stringvar_rolling_counts = tk.StringVar()
        self.stringvar_rolling_counts.set("0")
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
        label.grid(ipadx=int(self.DEFAULT_FONT_SIZE/3), sticky="E") # ipadx to create a little space in front of value

    def statistics_reset(self):
        first_active_column = self.dice_amount - 1
        last_active_column = self.dice_amount * 6 - 1
        for row, row_header in enumerate(self.stat_labels, 0):
            label_list = self.stat_labels[row_header]
            stringvar_list = self.stat_stringvars[row_header]
            for column in range(0, 6 * DICE_AMOUNT_MAX):
                label = label_list[column]
                stringvar_list[column].set("")
                if column < first_active_column or column > last_active_column:
                    label["bg"] = self.STATISTICS_INACTIVE_BG
                    label.master["bg"] = self.STATISTICS_INACTIVE_BG
                else:
                    label["bg"] = self.STATISTICS_ACTIVE_BG
                    label.master["bg"] = self.STATISTICS_ACTIVE_BG

    def statistics_update(self, dice_sum, counts, distribution):
        stringvar_list = self.stat_stringvars["Result Counts"]
        stringvar = stringvar_list[dice_sum - 1]
        stringvar.set(counts)
        stringvar_list = self.stat_stringvars["Distribution [%]"]
        stringvar = stringvar_list[dice_sum - 1]
        stringvar.set(distribution)


class DiceRolling():

    def __init__(self, data_to_gui, data_from_gui):
        thread_target = self.rolling_generator_thread
        thread_name = __class__.__name__ + "." + thread_target.__name__
        rolling_thread = threading.Thread(target=thread_target, name=thread_name, args=(data_from_gui, data_to_gui,))
        rolling_thread.setDaemon(True) # stop thread when script exits
        rolling_thread.start()

    def rolling_generator_thread(self, data_from_gui, data_to_gui):
        roll_result = DiceRollResult()
        start_rolling = True
        while True: # loop until the script is terminated (by user)
            if start_rolling:
                start_rolling = False
                print("== New Dice Rolling Session Started ==")
                number_of_dices = 1
                roll_result.init(number_of_dices)
            self.dice_roll(roll_result)
            time.sleep(DICE_ROLLING_INTERVAL)

    def dice_roll(self, roll_result):
        for dice_index in range(0, roll_result.number_of_dices):
            dice = random.randint(1, 6)
            roll_result.dices[dice_index] = dice
        roll_result.update_statistics()
        print_line = "Dice Roll " + roll_result.number_of_rollings_str + " ==> "
        for dice_index in range(0, roll_result.number_of_dices):
            dice = roll_result.dices[dice_index]
            if dice_index > 0:
                print_line += ", "
            print_line += DICE_SYMBOLS[dice] + "=" + str(dice)
        print(print_line)

    def create_gui_data(self):
        pass

class DiceRollResult():

    def __init__(self):
        self.statistics_results = DICE_AMOUNT_MAX * 6
        self.dices = [0] * self.statistics_results
        self.statistics_counts = [0] * self.statistics_results
        self.statistics_distribution = [0] * self.statistics_results

    def init(self, number_of_dices):
        self.number_of_rollings = 0
        self.number_of_dices = number_of_dices
        for index in range(0, self.statistics_results):
            self.statistics_counts[index] = 0
            self.statistics_distribution[index] = 0

    def update_statistics(self):
        self.number_of_rollings += 1
        self.number_of_rollings_str = str(self.number_of_rollings)
        self.sum = 0
        for dice_index in range(0, self.number_of_dices):
            self.sum += self.dices[dice_index]
        self.statistics_counts[self.sum-1] += 1
        for index in range(0, self.statistics_results):
            self.statistics_distribution[index] = self.statistics_counts[index] / self.number_of_rollings * 100
        print(self.statistics_counts)
        print(self.statistics_distribution)



data_to_gui = None
data_from_gui = None

rolling_generator = DiceRolling(data_to_gui, data_from_gui)

DiceGui()
