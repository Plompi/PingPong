import pygame

class Button:
    def __init__(self,text:str,size:int,position:tuple,textcolor,selected):
        self.__font = pygame.font.Font('freesansbold.ttf',size)
        self.__text = text
        self.__textcolor = textcolor
        self.__textrendered = self.__font.render(str(self.__text),True,self.__textcolor)
        self.__textrect = self.__textrendered.get_rect()
        self.__x,self.__y = position[0]-self.__textrendered.get_width()/2,position[1]-self.__textrendered.get_height()/2

    def Buttonreturn(self):
        return self.__textrendered,self.__textrect

    def position(self):
        return self.__x,self.__y

    def setSelected(self,selected):
        self.__selected = selected
        if selected == True:
            self.__textrendered = self.__font.render(str(self.__text),True,(255,255,120))
        else:
            self.__textrendered = self.__font.render(str(self.__text),True,(255,255,255))
