from tkinter import *
import numpy as np
from math import *
import keyboard

tk = Tk()
cnv=Canvas(tk, width=500, height=500, bg="black")
cnv.pack(padx=0, pady=0)

#-------------------------------------------------------------------------------------------------------------------------------------------
#variables initiales

prex = 0
prey = 0
distance = 5

#-------------------------------------------------------------------------------------------------------------------------------------------
#class

class box(object):
    def __init__(self):
        self.alphax = 0
        self.alphay = 0
        self.alphaz = 0
        self.points =  [[[1], [1], [1]],
                        [[1], [1], [-1]],
                        [[1], [-1], [1]],
                        [[1], [-1], [-1]],
                        [[-1], [1], [1]],
                        [[-1], [1], [-1]],
                        [[-1], [-1], [1]],
                        [[-1], [-1], [-1]]]
        self.dots = [n for n in range(8)]

cube = box()

#-------------------------------------------------------------------------------------------------------------------------------------------
#init

def init():
    cnv.delete(ALL)

#-------------------------------------------------------------------------------------------------------------------------------------------
#matrix_mult

def matrix_mult(a, b):
    return 0

#-------------------------------------------------------------------------------------------------------------------------------------------
#draw

def draw(x, y, t):
    cnv.create_oval(x-50*t, y-50*t, x+50*t, y+50*t, fill="blue")

#-------------------------------------------------------------------------------------------------------------------------------------------
#control

def control():
    global distance
    if keyboard.is_pressed("r"):
        init()
    if keyboard.is_pressed("up"):
        distance += 0.2
    if keyboard.is_pressed("down"):
        distance -= 0.2
    if keyboard.is_pressed("right"):
        cube.alphaz += 0.1
    if keyboard.is_pressed("left"):
        cube.alphaz -= 0.1
        
#-------------------------------------------------------------------------------------------------------------------------------------------
#brain

def brain():
    global distance
    cnv.delete(ALL)
    rotationx = [[1, 0, 0],
                 [0, np.cos(cube.alphax), -np.sin(cube.alphax)],
                 [0, np.sin(cube.alphax), np.cos(cube.alphax)]]

    rotationy = [[np.cos(cube.alphay), 0, -np.sin(cube.alphay)],
                 [0, 1, 0],
                 [np.sin(cube.alphay), 0, np.cos(cube.alphay)]]

    rotationz = [[np.cos(cube.alphaz), -np.sin(cube.alphaz), 0],
                 [np.sin(cube.alphaz), np.cos(cube.alphaz), 0],
                 [0, 0, 1]]
    
    for point in cube.points:
        cube_2d = np.dot(rotationx, point)
        cube_2d = np.dot(rotationy, cube_2d)
        cube_2d = np.dot(rotationz, cube_2d)

        z = 1/(distance - cube_2d[2][0])
        projection_matrix = [[z, 0, 0], [0, z, 0]]

        projection = np.dot(projection_matrix, cube_2d)

        x = int(projection[0][0]*300)+250
        y = int(projection[1][0]*300)+250

        draw(x, y, z)

#-------------------------------------------------------------------------------------------------------------------------------------------
#move

def move(pos):
    global prex, prey
    cube.alphay += -(pos.x-prex)/100
    cube.alphax += -(pos.y-prey)/100
    prex = pos.x
    prey = pos.y

#-------------------------------------------------------------------------------------------------------------------------------------------
#newpos

def newpos(pos):
    global prex, prey
    prex = pos.x
    prey = pos.y

#-------------------------------------------------------------------------------------------------------------------------------------------
#main

def main():
    control()
    brain()
    tk.bind("<B1-Motion>", move)
    tk.bind("<Button-1>", newpos)
    tk.after(15, main)

#-------------------------------------------------------------------------------------------------------------------------------------------

init()
main()
tk.mainloop()