import pygame
from pygame import gfxdraw
from random import choice

class Ball:
    def __init__(self,position:tuple,win,scheme):
        self.__scheme = scheme
        self.__x,self.__y = position[0],position[1]
        self.__speedx = 0
        self.__speedy = 0
        self.__timer = pygame.time.get_ticks()
        self.__win = win
        self.__ball = pygame.Rect(self.__x, self.__y, 32, 32)
        self.__color = self.__scheme.hex_to_rgb(self.__scheme.loadactivecolor()[4])

    def changePosition(self,player1,player2):
        self.__player1Rect,self.__player2Rect = player1.getRect(),player2.getRect()
        if self.__ball.left <= 0 or self.__ball.right >= self.__win.get_width():
            self.__timer = pygame.time.get_ticks()
            if self.__ball.left <= 0:
                player2.setPoints()
            else:
                player1.setPoints()
            self.__x,self.__y = self.__win.get_width()/2-16,self.__win.get_height()/2-16
            self.__speedx,self.__speedy = 0,0

        if self.__ball.top <= 0 or self.__ball.bottom >= self.__win.get_height():
            self.__speedy*=-1

        if self.__ball.colliderect(self.__player1Rect) or self.__ball.colliderect(self.__player2Rect):
            self.__cp = self.__player1Rect
            if self.__ball.colliderect(self.__player2Rect):
                self.__cp = self.__player2Rect

            if (abs(self.__cp.bottom - self.__ball.top) <= 10 and self.__speedy < 0) or (abs(self.__cp.top - self.__ball.bottom) <= 10 and self.__speedy > 0):
                self.__speedx += (self.__speedx / abs(self.__speedx))*0.08
                self.__speedy*=-1
                self.__speedy += (self.__speedy / abs(self.__speedy))*0.08
            if (abs(self.__cp.right - self.__ball.left) <= 10 and self.__speedx < 0) or abs(self.__cp.left - self.__ball.right) <= 10 and self.__speedx > 0:
                self.__speedx*=-1
                self.__speedy += (self.__speedy / abs(self.__speedy))*0.08
                self.__speedx += (self.__speedx / abs(self.__speedx))*0.08
        
        self.__x += self.__speedx
        self.__y += self.__speedy
        self.__ball = pygame.Rect(self.__x,self.__y, 32, 32)
        pygame.gfxdraw.aacircle(self.__win, int(self.__x)+16 ,int(self.__y)+16, 16, self.__color)
        pygame.gfxdraw.filled_circle(self.__win, int(self.__x)+16, int(self.__y)+16, 16, self.__color)

    def getSpeed(self):
        return self.__speedx

    def reset(self):
        self.__speedx,self.__speedy = choice([2,-2]),choice([2,-2])

    def restart(self):
        self.__timer = pygame.time.get_ticks()
        self.__speedx,self.__speedy = 0,0

    def getTimer(self):
        return self.__timer

    def setTimer(self,n):
        self.__timer = n