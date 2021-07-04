from tkinter import *
import numpy as np
from math import *
import keyboard

tk = Tk()
cnv=Canvas(tk, width=500, height=500, bg="black")
cnv.pack(padx=0, pady=0)

#-------------------------------------------------------------------------------------------------------------------------------------------
#variables initiales

#-------------------------------------------------------------------------------------------------------------------------------------------
#class

class point(object):
    def __init__(self):
        self.alphax = 0
        self.alphay = 0
        self.x = [-1, 1, 1, -1]
        self.y = [-1, -1, 1, 1]

cube = point()

#-------------------------------------------------------------------------------------------------------------------------------------------
#init

def init():
    pass

#-------------------------------------------------------------------------------------------------------------------------------------------
#draw

def draw():
    cnv.delete(ALL)
    cnv.create_line(cube.x[0]*100+250, cube.y[0]*100+250, cube.x[1]*100+250, cube.y[1]*100+250, width=5, fill="blue")
    cnv.create_line(cube.x[1]*100+250, cube.y[1]*100+250, cube.x[2]*100+250, cube.y[2]*100+250, width=5, fill="yellow")
    cnv.create_line(cube.x[2]*100+250, cube.y[2]*100+250, cube.x[3]*100+250, cube.y[3]*100+250, width=5, fill="red")
    cnv.create_line(cube.x[3]*100+250, cube.y[3]*100+250, cube.x[0]*100+250, cube.y[0]*100+250, width=5, fill="green")

    cnv.create_oval(cube.x[0]*100+250-3, cube.y[0]*100+250-3, cube.x[0]*100+250+3, cube.y[0]*100+250+3, fill="white")
    cnv.create_oval(cube.x[1]*100+250-3, cube.y[1]*100+250-3, cube.x[1]*100+250+3, cube.y[1]*100+250+3, fill="white")
    cnv.create_oval(cube.x[2]*100+250-3, cube.y[2]*100+250-3, cube.x[2]*100+250+3, cube.y[2]*100+250+3, fill="white")
    cnv.create_oval(cube.x[3]*100+250-3, cube.y[3]*100+250-3, cube.x[3]*100+250+3, cube.y[3]*100+250+3, fill="white")

#-------------------------------------------------------------------------------------------------------------------------------------------
#control

def control():
    global player_playing
    if keyboard.is_pressed("r"):
        cnv.delete(ALL)
        init()
    if keyboard.is_pressed("up"):
        cube.alphay += 0.02
    if keyboard.is_pressed("down"):
        cube.alphay += -0.02
    if keyboard.is_pressed("right"):
        cube.alphax += 0.02
    if keyboard.is_pressed("left"):
        cube.alphax += -0.02

#-------------------------------------------------------------------------------------------------------------------------------------------
#brain

def brain():
    cube.x[0] = -np.cos(cube.alphax)+0.5*np.sin(cube.alphay)
    cube.x[1] = np.cos(cube.alphax)+0.5*np.sin(cube.alphay)
    cube.x[2] = np.cos(cube.alphax)-0.5*np.sin(cube.alphay)
    cube.x[3] = -np.cos(cube.alphax)-0.5*np.sin(cube.alphay)
    cube.y[0] = np.cos(cube.alphay)-0.5*np.sin(cube.alphax)
    cube.y[1] = np.cos(cube.alphay)+0.5*np.sin(cube.alphax)
    cube.y[2] = -np.cos(cube.alphay)+0.5*np.sin(cube.alphax)
    cube.y[3] = -np.cos(cube.alphay)-0.5*np.sin(cube.alphax)

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