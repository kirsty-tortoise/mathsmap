import tkinter as tk
from tkinter import ttk as ttk

class Application():
    def __init__(self, master):
        self.master = master
        self.menus = tk.Menu(master)
        master.config(menu=self.menus)

        self.file = tk.Menu(self.menus, tearoff=0)
        self.menus.add_cascade(label="File", menu=self.file)
        self.file.add("command", label="New")
        self.file.add("command", label="Save")
        self.file.add("command", label="HELP!!!")

        self.edit = tk.Menu(self.menus, tearoff=0)
        self.menus.add_cascade(label="Edit", menu=self.edit)
        self.edit.add("command", label="Undo")
        self.edit.add("command", label="Redo")

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
        if event.delta > 0:
            self.canvas.yview_scroll(-1, "units")
        else:
            self.canvas.yview_scroll(1, "units")
    
    def destroy(self):
        for child in self.master.winfo_children():
            child.destroy()