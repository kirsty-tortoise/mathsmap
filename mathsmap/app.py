"""
Main application file
Defines a control class then makes a controller that sets up the window.
"""

import tkinter as tk
from mathsmap.home import Home
from mathsmap.explore import Explore

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

root = tk.Tk()
controller = Control(root)
root.mainloop()
