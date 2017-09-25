import tkinter as tk
from tkinter import ttk as ttk
from PIL import ImageTk

class Home():
    def __init__(self, master, controller):
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
        for child in self.master.winfo_children():
            child.destroy()