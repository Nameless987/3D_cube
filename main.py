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
        self.alphax = -np.pi/2
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
        self.dots = [[0, 0, 0] for n in range(8)]

cube = box()

class play(object):
    global distance
    def __init__(self):
        self.x = 5
        self.y = 0
        self.z = 0

player = play()

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

def draw():
    for dot in cube.dots:
        cnv.create_oval(dot[0]-50*dot[2], dot[1]-50*dot[2], dot[0]+50*dot[2], dot[1]+50*dot[2], fill="blue")
    
    cnv.create_line(cube.dots[0][0], cube.dots[0][1], cube.dots[1][0], cube.dots[1][1], width=1, fill="white")
    cnv.create_line(cube.dots[1][0], cube.dots[1][1], cube.dots[3][0], cube.dots[3][1], width=1, fill="white")
    cnv.create_line(cube.dots[0][0], cube.dots[0][1], cube.dots[2][0], cube.dots[2][1], width=1, fill="white")
    cnv.create_line(cube.dots[2][0], cube.dots[2][1], cube.dots[3][0], cube.dots[3][1], width=1, fill="white")

    cnv.create_line(cube.dots[4][0], cube.dots[4][1], cube.dots[5][0], cube.dots[5][1], width=1, fill="white")
    cnv.create_line(cube.dots[5][0], cube.dots[5][1], cube.dots[7][0], cube.dots[7][1], width=1, fill="white")
    cnv.create_line(cube.dots[4][0], cube.dots[4][1], cube.dots[6][0], cube.dots[6][1], width=1, fill="white")
    cnv.create_line(cube.dots[6][0], cube.dots[6][1], cube.dots[7][0], cube.dots[7][1], width=1, fill="white")
    
    cnv.create_line(cube.dots[0][0], cube.dots[0][1], cube.dots[4][0], cube.dots[4][1], width=1, fill="white")
    cnv.create_line(cube.dots[1][0], cube.dots[1][1], cube.dots[5][0], cube.dots[5][1], width=1, fill="white")
    cnv.create_line(cube.dots[3][0], cube.dots[3][1], cube.dots[7][0], cube.dots[7][1], width=1, fill="white")
    cnv.create_line(cube.dots[2][0], cube.dots[2][1], cube.dots[6][0], cube.dots[6][1], width=1, fill="white")

#-------------------------------------------------------------------------------------------------------------------------------------------
#control

def control():
    if keyboard.is_pressed("r"):
        init()
    if keyboard.is_pressed("z"):
        player.x -= 0.1
    if keyboard.is_pressed("s"):
        player.x += 0.1
    if keyboard.is_pressed("d"):
        player.y -= 0.1
    if keyboard.is_pressed("q"):
        player.y += 0.1
    if keyboard.is_pressed("space"):
        player.z += 0.1
    if keyboard.is_pressed("shift"):
        player.z -= 0.1
    if keyboard.is_pressed("a"):
        cube.alphay -= 0.025
    if keyboard.is_pressed("e"):
        cube.alphay += 0.025

    cube.points =  [[[1+player.y], [1+player.x], [1+player.z]],
                    [[1+player.y], [1+player.x], [-1+player.z]],
                    [[1+player.y], [-1+player.x], [1+player.z]],
                    [[1+player.y], [-1+player.x], [-1+player.z]],
                    [[-1+player.y], [1+player.x], [1+player.z]],
                    [[-1+player.y], [1+player.x], [-1+player.z]],
                    [[-1+player.y], [-1+player.x], [1+player.z]],
                    [[-1+player.y], [-1+player.x], [-1+player.z]]]
        
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

    i = 0
    
    for point in cube.points:
        cube_2d = np.dot(rotationy, point)
        cube_2d = np.dot(rotationz, cube_2d)
        cube_2d = np.dot(rotationx, cube_2d)

        z = 1/(np.abs(player.y) - cube_2d[2][0])
        projection_matrix = [[z, 0, 0], [0, z, 0]]

        projection = np.dot(projection_matrix, cube_2d)

        x = int(projection[0][0]*300)+250
        y = int(projection[1][0]*300)+250

        cube.dots[i] = [x, y, z]
        i += 1
    
    print(player.x)

#-------------------------------------------------------------------------------------------------------------------------------------------
#move

def move(pos):
    global prex, prey
    cube.alphaz -= -(pos.x-prex)/300
    cube.alphax += -(pos.y-prey)/300
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
    draw()
    tk.bind("<B1-Motion>", move)
    tk.bind("<Button-1>", newpos)
    tk.after(15, main)

#-------------------------------------------------------------------------------------------------------------------------------------------

init()
main()
tk.mainloop()