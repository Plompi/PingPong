import pygame

class Button:
    def __init__(self,text:str,size:int,position:tuple,scheme,win,selected):
        self.__win = win
        self.__scheme = scheme
        self.__selected = selected
        self.__color = self.__scheme.loadactivecolor()[1:4]
        self.__font = pygame.font.SysFont(None,size)
        self.__text = text
        self.__textrendered = self.__font.render(self.__text,True,self.__color[self.__selected])
        self.__textrect = self.__textrendered.get_rect()
        self.__x,self.__y = position[0]-self.__textrendered.get_width()/2,position[1]-self.__textrendered.get_height()/2

    def position(self):
        return (self.__x,self.__y),(self.__textrect.width,self.__textrect.height)

    def setSelected(self):
        self.__selected*=-1
        self.__textrendered = self.__font.render(self.__text,True,self.__color[self.__selected])

    def draw(self):
        self.__win.blit(self.__textrendered,(self.__x,self.__y))

    def change_color(self):
        self.__color = self.__scheme.loadactivecolor()[1:4]
        self.__textrendered = self.__font.render(self.__text,True,self.__color[self.__selected])