"""
Defines a class to set up and run the home screen.
"""

import tkinter as tk
from tkinter import ttk as ttk
from PIL import ImageTk

class Home:
    """
    A class that sets up and runs the home screen.
    """
    def __init__(self, master, controller):
        """
        Sets up the home screen with navigation buttons.
        """
        self.master = master
        self.controller = controller

        self.images = []
        images = [("plus", None), ("explore", self.controller.explore), ("diary", None)]
        for file_name, callback in images:
            new_button = tk.Button(master)
            image = ImageTk.PhotoImage(file="assets/"+file_name+".png")
            self.images.append(image)
            new_button.config(image=image, compound=tk.RIGHT, command=callback)
            new_button.pack(side=tk.LEFT)

    def destroy(self):
        """
        Destroys all widgets in the home screen.
        """
        for child in self.master.winfo_children():
            child.destroy()