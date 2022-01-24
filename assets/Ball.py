import pygame
from random import choice
from pygame import gfxdraw

class Ball:
    def __init__(self,position:tuple,win):
        self.__x,self.__y = position[0],position[1]
        self.__speedx = 0
        self.__speedy = 0
        self.__timer = pygame.time.get_ticks()
        self.__win = win
        self.__ball = pygame.Rect(self.__x, self.__y, 32, 32)

    def changePosition(self,player1,player2):
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

        if self.__ball.colliderect(player1.getRect()) or self.__ball.colliderect(player2.getRect()):
            if (abs(player1.getRect().bottom - self.__ball.top) <= 10 and self.__speedy < 0) or (abs(player1.getRect().top - self.__ball.bottom) <= 10 and self.__speedy > 0):
                self.__speedy*=-1
            if (abs(player1.getRect().right - self.__ball.left) <= 10 and self.__speedx < 0) or abs(player1.getRect().left - self.__ball.right) <= 10 and self.__speedx > 0:
                self.__speedx*=-1
            if (abs(player2.getRect().bottom - self.__ball.top) <= 10 and self.__speedy < 0) or (abs(player2.getRect().top - self.__ball.bottom) <= 10 and self.__speedy > 0):
                self.__speedy*=-1
            if (abs(player2.getRect().right - self.__ball.left) <= 10 and self.__speedx < 0) or abs(player2.getRect().left - self.__ball.right) <= 10 and self.__speedx > 0:
                self.__speedx*=-1
        
        self.__x += self.__speedx
        self.__y += self.__speedy
        self.__ball = pygame.Rect(self.__x,self.__y, 32, 32)
        gfxdraw.aacircle(self.__win, int(self.__x)+16 ,int(self.__y)+16, 16, (135,146,163))
        gfxdraw.filled_circle(self.__win, int(self.__x)+16, int(self.__y)+16, 16, (135,146,163))

    def getRect(self):
        return self.__ball

    def getSpeed(self):
        return self.__speedx

    def setSpeed(self):
        self.__speedx,self.__speedy = 2*choice([1,-1]),2*choice([1,-1])

    def getTimer(self):
        return self.__timer