import pygame

class Button:
    def __init__(self,text:str,size:int,position:tuple,scheme,win):
        self.__win = win
        self.__scheme = scheme
        self.__color = self.__scheme.loadactivecolor()
        self.__font = pygame.font.SysFont('freesansbold.ttf',size)
        self.__text = text
        self.__textrendered = self.__font.render(str(self.__text),True,self.__color[2])
        self.__textrect = self.__textrendered.get_rect()
        self.__x,self.__y = position[0]-self.__textrendered.get_width()/2,position[1]-self.__textrendered.get_height()/2

    def position(self):
        return (self.__x,self.__y),(self.__textrect.width,self.__textrect.height)

    def setSelected(self,selected):
        self.__color = self.__scheme.loadactivecolor()
        if selected == True:
            self.__textrendered = self.__font.render(str(self.__text),True,self.__color[3])
        else:
            self.__textrendered = self.__font.render(str(self.__text),True,self.__color[2])

    def draw(self):
        self.__win.blit(self.__textrendered,(self.__x,self.__y))
