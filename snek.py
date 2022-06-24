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
    body = []
    turns = {}

    def __init__(self, color, pos):
        self.color = color
        self.head = cube(pos) # the head of the snake is equal to a cube at the given position that is passed from the init
        self.body.apppend(self.head)
        self.dirnx = 0
        self.dirny = 1

    def move(self):
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()

            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.dirnx = -1 # pygame processes the windows from top left to right and down, so the lower the value the closer to the left you are
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_RIGHT]:
                    self.dirnx = 1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_UP]:
                    self.dirnx = 0
                    self.dirny = -1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_DOWN]:
                    self.dirnx = 0
                    self.dirny = 1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

            for i, c in enumerate(self.body):
                p = c.pos[:]
                if p in self.turns:
                    turn = self.turns[p]
                    c.move(turn[0], turn[1])
                    if i == len(self.body)-1:
                        self.turns.pop()

    def reset(self, pos):
        pass
    def add_cube(self):
        pass
    def draw(self, surface):
        pass

def draw_grid(w, rows, surface):
    size_btwn = w // rows

    x = 0 
    y = 0
    for l in range (rows):
        x = x + size_btwn
        y = y + size_btwn

        pygame.draw.line(surface, (255, 255, 255), (x,0), (x,w)) # draws the lines and starts with the x and y variables indicating the position of the line // vertical line
        pygame.draw.line(surface, (255, 255, 255), (0,y), (w,y)) # draws the lines and starts with the x and y variables indicating the position of the line // horizontal line

def redraw_window(surface):
    global rows, width
    surface.fill((0,0,0))
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
        clock.tick(10) # forces the game to run in 10 fps
        redraw_window(win)
    pass

main()