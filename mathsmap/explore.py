"""
Defines a class to set up and run the explore screen.
"""

import tkinter as tk
from tkinter import ttk as ttk

from mathsmap.screen import Screen

class Explore(Screen):
    """
    A class that sets up and runs the explore screen.
    """
    def __init__(self, master, controller):
        """
        Sets up the explore screen with:
         - A menu
         - A lecture list
         - An area for flashcards
        """
        super().__init__(master, controller)

        self.left_frame = tk.Frame(master, background="#000000")
        self.left_frame.pack(side=tk.LEFT, expand=tk.YES, fill=tk.BOTH)

        self.canvas = tk.Canvas(self.left_frame, bg="#99e6ff",
                                height=500, width=500, scrollregion=(0, 0, 500, 1000))
        self.canvas.pack(fill=tk.Y, expand=tk.YES, side=tk.LEFT)
        self.canvas.bind("<MouseWheel>", self.mouse_wheel)

        self.canvas_scroll = ttk.Scrollbar(self.left_frame, command=self.canvas.yview)
        self.canvas_scroll.pack(side=tk.LEFT, fill=tk.Y)
        self.canvas["yscrollcommand"] = self.canvas_scroll.set


        self.right_frame = tk.Frame(master)
        self.right_frame.pack(side=tk.LEFT, fill=tk.Y)

        self.lists = tk.Listbox(self.right_frame, width=30)
        self.lists.pack(side=tk.LEFT, fill=tk.Y)
        self.lists.insert(tk.END, *["Lecture " + str(i) for i in range(1, 13)])

        self.scroll = ttk.Scrollbar(self.right_frame, command=self.lists.yview)
        self.scroll.pack(side=tk.LEFT, fill=tk.Y)

        self.lists["yscrollcommand"] = self.scroll.set

    def mouse_wheel(self, event):
        """
        Handles mouse_wheel events for the flashcard area.
        """
        if event.delta > 0:
            self.canvas.yview_scroll(-1, "units")
        else:
            self.canvas.yview_scroll(1, "units")
