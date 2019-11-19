#!/usr/bin/env python

import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.configure(background='white')
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self, bg="white")
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")
        self.quit = tk.Button(self, text="QUIT", fg="red", bg="#abcdef", command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")


root = tk.Tk()
app = Application(master=root)
app.master.title("This is a test")
app.master.minsize(1024, 768)
app.master.maxsize(1024, 768)
app.mainloop()
