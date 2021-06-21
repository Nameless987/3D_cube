from tkinter import *
import numpy as np
from math import *
import keyboard

tk = Tk()
cnv=Canvas(tk, width=500, height=500, bg="white")
cnv.pack(padx=0, pady=0)

#-------------------------------------------------------------------------------------------------------------------------------------------
#variables initiales

#-------------------------------------------------------------------------------------------------------------------------------------------
#class

class point(object):
    def __init__(self):
        self.alphax = 0
        self.alphay = 0
        self.alphaz = 0
        self.x = [0, 1, 0, 1, 0, 1, 0, 1]
        self.y = [0, 0, 1, 1, 0, 0, 1, 1]
        self.z = [0, 0, 0, 0, 1, 1, 1, 1]

cube = point()

#-------------------------------------------------------------------------------------------------------------------------------------------
#init

def init():
    pass

#-------------------------------------------------------------------------------------------------------------------------------------------
#draw

def draw():
    cnv.delete(ALL)
    pass

#-------------------------------------------------------------------------------------------------------------------------------------------
#control

def control():
    global player_playing
    if keyboard.is_pressed("r"):
        cnv.delete(ALL)
        init()
    if keyboard.is_pressed("up"):
        pass
    if keyboard.is_pressed("down"):
        pass
    if keyboard.is_pressed("right"):
        pass
    if keyboard.is_pressed("left"):
        pass

#-------------------------------------------------------------------------------------------------------------------------------------------
#brain

def brain():
    pass

#-------------------------------------------------------------------------------------------------------------------------------------------
#main

def main():
    control()
    brain()
    draw()
    tk.after(5, main)

#-------------------------------------------------------------------------------------------------------------------------------------------

init()
main()
tk.mainloop()