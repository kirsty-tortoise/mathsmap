"""
Main application file
Defines a control class then makes a controller that sets up the window.
"""

import tkinter as tk
from mathsmap.home import Home
from mathsmap.explore import Explore
from mathsmap.new_map import NewMap

class Control:
    """
    A control class which switches between screens.
    """
    def __init__(self, root):
        """
        Sets up the home screen.
        """
        self.root = root
        self.app = Home(root, self)

    def explore(self):
        """
        Switches to the explore view (used as callback)
        """
        self.app.destroy()
        self.app = Explore(root, controller)
    
    def new_map(self):
        """
        Creates a new map (used as callback)
        """
        self.wizard = NewMap(self)


root = tk.Tk()
controller = Control(root)
root.mainloop()
