"""
Contains classes controlling wizards for making new maps
"""

import tkinter as tk
import mathsmap.colours as colours

class Wizard:
    """
    A base class for all wizards in this project
    """
    def clear(self):
        """
        Remove all current widgets from top level of wizard
        """
        for child in self.top.winfo_children():
            child.destroy()

class NewMap(Wizard):
    """
    Class for any new map
    """
    def __init__(self, controller):
        """
        Set up NewMap wizard
        """
        self.controller = controller
        self.top = tk.Toplevel()
        self.top.title("Make a new map")
        self.welcome_screen()

    def welcome_screen(self):
        """
        Sets up first screen of wizard
        """
        self.clear()
        self.scheme = colours.BLUESCHEME
        self.background = self.scheme.lighter
        self.top.configure(background=self.background)
        self.title = tk.Label(self.top, text="Let's make a new map!", font=(None, 20),
                              background=self.background)
        self.title.grid(row=0, column=0, columnspan=2)
        self.text = tk.Label(self.top,
                             text=("When do you need to make your mathsmap? " +
                                   "Is it right now, possibly in a rush before exams, " +
                                   "or over time, while you attend lectures and learn?"),
                             wraplength=400, background=self.background
                            )
        self.text.grid(row=1, column=0, columnspan=2)
        buttons_needed = [("Right now!", 0),
                          ("Over time!", 1)]
        for text, column in buttons_needed:
            button = tk.Button(self.top, text=text, width=15, height=3, 
                               background=self.scheme.darkest, activebackground=self.scheme.darker,
                               foreground="white", font=(None, 15))
            button.grid(row=2, column=column, pady=5)

    def clear(self):
        """
        Remove all current widgets from top level
        """
        for child in self.top.winfo_children():
            child.destroy()

class NewFutureMap(Wizard):
    """
    Class for new maps to be added to slowly in the future
    """
    pass

class NewNowMap(Wizard):
    """
    Class for new maps to be added to and completed right now
    """
    pass
