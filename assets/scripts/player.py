import pygame

class Spieler:
    def __init__(self,position:tuple,win,scheme):
        self.__position = position
        self.__x,self.__y = self.__position[0],self.__position[1]-50
        self.__win = win
        self.__scheme = scheme
        self.__color = self.__scheme.loadactivecolor()[3]
        self.__speed = 4
        self.__player = pygame.Rect(self.__x, self.__y, 5, 100)
        self.__Input = (False,False) #top,bottom
        self.__Points = 0

    def changePosition(self):
        if self.__Input[0] and not self.__Input[1] and self.__y - self.__speed >= 0:
            self.__y -=self.__speed
        if self.__Input[1] and not self.__Input[0] and self.__y + self.__player.height + self.__speed <= self.__win.get_height(): #Höhe des Fensters
            self.__y += self.__speed
        self.__player = pygame.Rect(self.__x,self.__y, 5, 100)
        pygame.draw.rect(self.__win, self.__color, self.__player,0,20)

    def setInput(self,newInput:tuple):
        self.__Input= newInput

    def getRect(self):
        return self.__player
    
    def setPoints(self):
        self.__Points+= 1

    def getPoints(self):
        return self.__Points

    def restart(self):
        self.__Points = 0
        self.__x,self.__y = self.__position[0],self.__position[1]-50
        pygame.Rect(self.__x, self.__y, 5, 100)