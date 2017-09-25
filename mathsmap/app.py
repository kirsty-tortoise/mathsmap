import tkinter as tk
from tkinter import ttk as ttk
from mathsmap.home import Home
from mathsmap.explore import Application

class Control():
    def __init__(self, root):
        self.root = root
        self.app = Home(root, self)

    def explore(self):
        self.app.destroy()
        self.app = Application(root)

root = tk.Tk()
controller = Control(root)
root.mainloop()
