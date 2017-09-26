"""
Implements the base class screen.
This provides basic functionality for home screen, explore screen, etc.
"""

import tkinter as tk

class Screen:
    """
    A base class that specific screens can inherit from.
    """
    def __init__(self, master, controller):
        self.master = master
        self.controller = controller
        self.menus = tk.Menu(master)
        self.master.config(menu=self.menus)

        menus_needed = [("File", ["New", "Save", "HELP!!!"]),
                        ("Edit", ["Undo", "Redo"])]
        for (menu_name, items) in menus_needed:
            new_menu = tk.Menu(self.menus, tearoff=0)
            self.menus.add_cascade(label=menu_name, menu=new_menu)
            for item_name in items:
                new_menu.add("command", label=item_name)

    def destroy(self):
        """
        Destroys all widgets currently in the screen.
        """
        for child in self.master.winfo_children():
            child.destroy()
