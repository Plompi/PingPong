import sys
from os import path
from button import *
from main import *
from colorschemes import *
import pygame
from pygame import gfxdraw


class Menu:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('PingPong')
        pygame.display.set_icon(pygame.image.load("assets/img/icon.png"))
        self.__button_sound = pygame.mixer.Sound("assets/sounds/button.wav")
        pygame.mixer.music.load("assets/sounds/menu.wav")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.1)
        self.__button_sound.set_volume(0.2)
        self.__scheme = colorschemes()
        self.__color = self.__scheme.loadactivecolor()
        self.__win = pygame.display.set_mode((933,700))
        self.__clock = pygame.time.Clock()
        self.__selected = 1
        self.__buttons = [
            Button('PINGPONG',100,(self.__win.get_width()/2,self.__win.get_height()/2-300),self.__scheme,self.__win,1),
            Button('PLAY',100,(self.__win.get_width()/2,self.__win.get_height()/2-80),self.__scheme,self.__win,-1),
            Button('COLOR',100,(self.__win.get_width()/2,self.__win.get_height()/2),self.__scheme,self.__win,1),
            Button('QUIT',100,(self.__win.get_width()/2,self.__win.get_height()/2+80),self.__scheme,self.__win,1)
        ]
    def start(self):
        while True:
            for event in pygame.event.get():
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) or event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_w or event.key == pygame.K_UP) and self.__selected != 1:
                        self.__button_sound.play()
                        self.__buttons[self.__selected-1].setSelected()
                        self.__buttons[self.__selected].setSelected()
                        self.__selected -=1

                    if (event.key == pygame.K_s or event.key == pygame.K_DOWN) and self.__selected != 3:
                        self.__button_sound.play()
                        self.__buttons[self.__selected+1].setSelected()
                        self.__buttons[self.__selected].setSelected()
                        self.__selected +=1

                    if self.__selected == 2:
                        if (event.key == pygame.K_d or event.key == pygame.K_RIGHT) or (event.key == pygame.K_a or event.key == pygame.K_LEFT):
                            self.__button_sound.play()
                            self.__direction = 1
                            if (event.key == pygame.K_a or event.key == pygame.K_LEFT):
                                self.__direction = -1
                            self.__index = self.__scheme.indexofcolor(self.__scheme.loadactivecolor())
                            if self.__index[0]+self.__direction == self.__index[1]:
                                self.__scheme.setactivecolor(0)
                            else:
                                self.__scheme.setactivecolor(self.__index[0]+self.__direction)
                            self.__color = self.__scheme.loadactivecolor()
                            for i in self.__buttons:
                                i.change_color()


                    if event.key == pygame.K_RETURN:
                        if self.__selected == 1:
                            Fenster(self.__win,self.__scheme,self)
                            pygame.mixer.music.load("assets/sounds/menu.wav")
                            pygame.mixer.music.play(-1)

                        if self.__selected == 3:
                            pygame.quit()
                            sys.exit()

            self.__win.fill(self.__color[1])

            if self.__selected == 2:
                self.__left,self.__right = self.__buttons[2].position()[0][0],self.__buttons[2].position()[0][0] + self.__buttons[2].position()[1][0]
                self.__middletext = self.__buttons[2].position()[0][1] + (self.__buttons[2].position()[1][1]/2) - 4

                self.__newcolor = self.__scheme.hex_to_rgb(self.__color[2])
                gfxdraw.aapolygon(self.__win,[(self.__left-10, self.__middletext-20), (self.__left-10, self.__middletext+20), (self.__left-40, self.__middletext)],self.__newcolor)
                gfxdraw.filled_polygon(self.__win,[(self.__left-11, self.__middletext-19), (self.__left-11, self.__middletext+19), (self.__left-39, self.__middletext)],self.__newcolor)
                gfxdraw.aapolygon(self.__win,[(self.__right+10, self.__middletext-20), (self.__right+10, self.__middletext+20), (self.__right+40, self.__middletext)],self.__newcolor)
                gfxdraw.filled_polygon(self.__win,[(self.__right+11, self.__middletext-19), (self.__right+11, self.__middletext+19), (self.__right+39, self.__middletext)],self.__newcolor)

            for i in self.__buttons:
                i.draw()
            pygame.display.flip()
            self.__clock.tick(120)