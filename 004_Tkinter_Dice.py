""" import module functions (Python 3.xx) """
import random
import tkinter as tk # import all tkinter functions
import tkinter.font as tkfont

STATISTICS_HEADERS = ["Dice Sum", "Result Counts", "Distribution [%]"]
DICE_AMOUNT_MAX = 4


class DiceGui(tk.Tk): # Inheritance of tkinter to keep all GUI in it's own class

    # html symbols of dice 1 to 6 eyes (https://www.htmlsymbols.xyz/games-symbols/dice)
    DICE_SYMBOLS = ["\u2680", "\u2681", "\u2682", "\u2683", "\u2684", "\u2685"]

    FRAME_PADDING = 4
    DEFAULT_FONT_SIZE = 10
    DICE_FONT_SIZE = 128
    STATISTICS_COLUMN_WIDTH = 4
    STATISTICS_HEADER_BG = "light yellow"
    STATISTICS_ACTIVE_BG = "white"
    STATISTICS_INACTIVE_BG = "light gray"

    def __init__(self):
        tk.Tk.__init__(self)
        self.dice_values = [1, 2, 3, 4]
        self.dice_amount = 4
        self.default_font = tkfont.Font(size=self.DEFAULT_FONT_SIZE)
        self.stringvar_dice = self.dice_frame()
        self.dice_update()
        self.stat_labels, self.stat_stringvars = self.statistics_frame()
        self.statistics_reset()
        self.statistics_update(5, "8", "55.8")
        self.columnconfigure(0, weight=1)
        self.title("Dice Rolling Simulator")
        self.resizable(width=False, height=False)
        self.mainloop()

    def dice_frame(self):
        frame = tk.LabelFrame(self, text="Latest Dice Roll", font=self.default_font, labelanchor="n")
        frame.grid(padx=self.FRAME_PADDING, pady=self.FRAME_PADDING, sticky="EW")
        stringvar = tk.StringVar()
        font = tkfont.Font(size=self.DICE_FONT_SIZE)
        label = tk.Label(frame, textvariable=stringvar, fg="blue", font=font)
        label.grid()
        frame.columnconfigure(0, weight=1)
        return stringvar

    def dice_update(self):
        dice_value_text = ""
        for dice_value in self.dice_values:
            dice_value_text += self.DICE_SYMBOLS[dice_value-1]
        self.stringvar_dice.set(dice_value_text)

    def statistics_frame(self):
        stat_labels = {}
        stat_stringvars = {}
        statistics_frame = tk.LabelFrame(self, text="Statistics", font=self.default_font, labelanchor="n")
        statistics_frame.grid(padx=self.FRAME_PADDING, pady=(0, self.FRAME_PADDING))
        frame = tk.Frame(statistics_frame)
        frame.grid(padx=self.FRAME_PADDING*2, pady=self.FRAME_PADDING*2)
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
                        if row > 0: # new statistics row for containing values
                            stat_labels[row_header] = []
                            stat_stringvars[row_header] = []
                    else:
                        label["text"] = str(column)
                        label["width"] = self.STATISTICS_COLUMN_WIDTH
                        alignment = "EW"
                else: # statistics cell containing value
                    stringvar = tk.StringVar()
                    label["textvariable"] = stringvar
                    stat_labels[row_header].append(label)
                    stat_stringvars[row_header].append(stringvar)
                    alignment = "E"
                label.grid(column=column, row=row, sticky=alignment)
                cell.columnconfigure(0, weight=1)
        return stat_labels, stat_stringvars

    def statistics_reset(self):
        first_active_column = self.dice_amount - 1
        last_active_column = self.dice_amount * 6 - 1
        for row, row_header in enumerate(self.stat_labels, 0):
            label_list = self.stat_labels[row_header]
            stringvar_list = self.stat_stringvars[row_header]
            for column in range(0, 6 * DICE_AMOUNT_MAX):
                label = label_list[column]
                stringvar_list[column].set("")
                cell = label.master
                if column < first_active_column or column > last_active_column:
                    label["bg"] = self.STATISTICS_INACTIVE_BG
                    cell["bg"] = self.STATISTICS_INACTIVE_BG
                else:
                    label["bg"] = self.STATISTICS_ACTIVE_BG
                    cell["bg"] = self.STATISTICS_ACTIVE_BG

    def statistics_update(self, dice_sum, counts, distribution):
        stringvar_list = self.stat_stringvars["Result Counts"]
        stringvar = stringvar_list[dice_sum - 1]
        stringvar.set(counts)
        stringvar_list = self.stat_stringvars["Distribution [%]"]
        stringvar = stringvar_list[dice_sum - 1]
        stringvar.set(distribution)


DiceGui()