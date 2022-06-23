# Snake game 
# Made by enal

import math
import random
from turtle import width
import pygame
import tkinter as tk
from tkinter import messagebox

class cube(object):
    rows = 0
    w = 0
    def __init__(self, start, dirnx=1, dirny=0, color=(255, 0, 0)):
        pass
    def move(self, dirnx, dirny):
        pass
    def draw(self, surface, eyes=False):
        pass

class snake(object):
    def __init__(self, color, pos):
        pass
    def move(self):
        pass
    def reset(self, pos):
        pass
    def add_cube(self):
        pass
    def draw(self, surface):
        pass

def draw_grid(w, rows, surface):
    

def redraw_window(surface):
    global rows, width
    win.fill((0,0,0))
    draw_grid(width,rows,surface)
    pygame.display.update()

def random_snack(rows, items):
    pass
def message_box(subject, content):
    pass

def main():
    global width, rows
    width = 500
    height = 500
    rows = 20
    win = pygame.display.set_mode((width, width))
    s = snake((255,0,0), (10,10))
    flag = True

    clock = pygame.time.Clock()

    while flag:
        pygame.time.delay(50) # delays the game by a few miliseconds to ensure the program won't run too fast
        clock.tick(10) # forces the game to just run in 10 fps
        redraw_window(win)
    pass