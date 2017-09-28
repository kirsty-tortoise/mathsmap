"""
Contains classes controlling wizards for making new maps
"""

import tkinter as tk

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
        self.title = tk.Label(self.top, text="Let's make a new map!")
        self.title.pack()

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
