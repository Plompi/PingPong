import pygame
from player import *
from ball import *
from gameover import *
import sys

class Fenster:
    def __init__(self,win,scheme,menu):
        self.__menu = menu
        self.__pause = False
        self.__scheme = scheme
        self.__color = self.__scheme.loadactivecolor()
        self.__win = win
        self.__clock = pygame.time.Clock()
        self.__player1 = Spieler((20, self.__win.get_height()/2-(30/2)),self.__win,self.__scheme)
        self.__player2 = Spieler((self.__win.get_width()-20-5, self.__win.get_height()/2-(30/2)),self.__win,self.__scheme)
        self.__ball = Ball((self.__win.get_width()/2-16,self.__win.get_height()/2-16),self.__win,self.__scheme)
        self.__font = pygame.font.SysFont(None,50)

        while True:
            if self.__pause == False:
                for event in pygame.event.get():
                    self.__keys = pygame.key.get_pressed()
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                    if self.__keys[pygame.K_ESCAPE]:
                        del self.__player1,self.__player2,self.__ball
                        return
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        self.__timeCache = self.__timer -  self.__ball.getTimer()
                        self.__pause = True

                    self.__player1.setInput((self.__keys[pygame.K_w],self.__keys[pygame.K_s]))
                    self.__player2.setInput((self.__keys[pygame.K_UP],self.__keys[pygame.K_DOWN]))

                self.__win.fill(self.__color[1])
                pygame.draw.rect(self.__win, self.__color[2], pygame.Rect(self.__win.get_width()/2-2, 0, 5, self.__win.get_height()))
                self.__player1.changePosition()
                self.__player2.changePosition()
                self.__ball.changePosition(self.__player1,self.__player2)
                self.__score1 = self.__font.render(f"{self.__player1.getPoints()}",True,self.__color[2])
                self.__score2 = self.__font.render(f"{self.__player2.getPoints()}",True,self.__color[2])
                self.__win.blits([(self.__score1,(self.__win.get_width()/2-50-self.__score1.get_width(),self.__win.get_height()/2-self.__score1.get_height()/2)),
                                (self.__score2,(self.__win.get_width()/2+50,self.__win.get_height()/2-self.__score2.get_height()/2))])
                
                if self.__player1.getPoints() == 7 or self.__player2.getPoints() == 7 :
                    self.__winner = 1
                    if self.__player2.getPoints() == 7:
                        self.__winner = 2

                    if Gameover(self.__scheme,self.__win,f'PLAYER {self.__winner}',self.__menu):
                        self.__ball.restart()
                        self.__player1.restart()
                        self.__player2.restart()

                if self.__ball.getSpeed() == 0:
                    self.__timer = pygame.time.get_ticks()
                    if self.__timer -  self.__ball.getTimer() > 2100:
                        self.__timer = pygame.time.get_ticks()
                        self.__ball.reset()
                    if self.__timer -  self.__ball.getTimer() < 700:
                        self.__counter = self.__font.render('3',True,self.__color[3])
                        self.__win.blit(self.__counter,(self.__win.get_width()/2-self.__counter.get_width()/2,self.__win.get_height()/2+40))
                    if 700 < self.__timer -  self.__ball.getTimer() < 1400:
                        self.__counter = self.__font.render('2',True,self.__color[3])
                        self.__win.blit(self.__counter,(self.__win.get_width()/2-self.__counter.get_width()/2,self.__win.get_height()/2+40))
                    if 1400 < self.__timer -  self.__ball.getTimer() < 2100:
                        self.__counter = self.__font.render('1',True,self.__color[3])
                        self.__win.blit(self.__counter,(self.__win.get_width()/2-self.__counter.get_width()/2,self.__win.get_height()/2+40))
                pygame.display.flip()
                self.__clock.tick(120)

            if self.__pause == True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:

                        if event.key == pygame.K_ESCAPE:
                            return

                        if event.key == pygame.K_SPACE:
                            self.__ball.setTimer(pygame.time.get_ticks()-self.__timeCache)
                            self.__pause = False