import tkinter
from pprint import pprint
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import *
from PIL import Image, ImageTk
from functools import partial

class App():
    def __init__(self):
        self.name = "NAME"
        self.root = Tk()
        self.window_width = 800
        self.window_height = 520
        self.root.geometry(f"{str(self.window_width)}x{str(self.window_height)}")
        self.canvas = Canvas(self.root, width=800, height=400)
        self.canvas.grid(row=0, column=0, columnspan=3)
        self.t = Text(width=100, height=1)
        self.t.grid(row=1, columnspan=2)
        self.b1 = Button(text='Open', command=self.loadPhoto, width=50)
        self.b1.grid(row=2, column=0)
        self.b2 = Button(text="Save", width=50, command=self.savePhoto)
        self.b2.grid(row=2, column=1)
        self.root.mainloop()


    def loadPhoto(self):
        self.name = askopenfilename()
        if self.name:
            self.t.delete(0.0, END)
            self.t.insert(0.0, self.name)
            self.new = ImageTk.PhotoImage(Image.open(self.name))
            self.canvas['width'] = self.new.width()
            self.canvas['height'] = self.new.height()
            if self.new.height() > self.window_height - 120:
                self.window_height += self.new.height() - 400
                self.root.geometry(f"{str(self.window_width)}x{str(self.window_height)}")
            if self.new.height() < 400:
                self.window_height = 520
                self.root.geometry(f"{str(self.window_width)}x{str(self.window_height)}")
            self.canvas.create_image(self.new.width()/2, self.new.height()/2, image=self.new)
            self.canvas.create_oval(0, 0, 100, 100, width=1)





    def savePhoto(self):
        self.canvas.postscript(file="my_dram.ps", colormode="color")
        img = Image.open("my_dram.ps")
        img.save(f"{self.name}_water_marker.png", "png")

App()


