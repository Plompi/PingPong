import pygame
from Player import *
from Ball import *

class Fenster:
    def __init__(self,win):
        self.__win = win
        self.__clock = pygame.time.Clock()
        self.__player1 = Spieler((20, self.__win.get_height()/2-(30/2)),(171,178,191),self.__win)
        self.__player2 = Spieler((self.__win.get_width()-20-5, self.__win.get_height()/2-(30/2)),(171,178,191),self.__win)
        self.__ball = Ball((self.__win.get_width()/2-16,self.__win.get_height()/2-16),self.__win)
        self.__font = pygame.font.Font('freesansbold.ttf',32)

        while True:
            for event in pygame.event.get():
                self.__keys = pygame.key.get_pressed()
                if self.__keys[pygame.K_ESCAPE] or event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                self.__player1.setInput((self.__keys[pygame.K_w],self.__keys[pygame.K_s]))
                self.__player2.setInput((self.__keys[pygame.K_UP],self.__keys[pygame.K_DOWN]))
            self.__win.fill((40, 44, 52))
            pygame.draw.rect(self.__win, (33,36,43), pygame.Rect(self.__win.get_width()/2-2, 0, 5, self.__win.get_height()))
            self.__player1.changePosition()
            self.__player2.changePosition()
            self.__score1 = self.__font.render(str(self.__player1.getPoints()),True,(33,36,43))
            self.__score2 = self.__font.render(str(self.__player2.getPoints()),True,(33,36,43))
            self.__win.blit(self.__score1,(self.__win.get_width()/2-50-self.__score1.get_width(),self.__win.get_height()/2-self.__score1.get_height()/2))
            self.__win.blit(self.__score2,(self.__win.get_width()/2+50,self.__win.get_height()/2-self.__score2.get_height()/2))
            self.__ball.changePosition(self.__player1,self.__player2)
            if self.__ball.getSpeed() == 0:
                self.__timer = pygame.time.get_ticks()
                if self.__timer -  self.__ball.getTimer() > 2100:
                    self.__ball.setSpeed()
                if self.__timer -  self.__ball.getTimer() < 700:
                    self.__counter = self.__font.render('3',True,(171,178,191))
                    self.__win.blit(self.__counter,(self.__win.get_width()/2-self.__counter.get_width()/2,self.__win.get_height()/2+40))
                if 700 < self.__timer -  self.__ball.getTimer() < 1400:
                    self.__counter = self.__font.render('2',True,(171,178,191))
                    self.__win.blit(self.__counter,(self.__win.get_width()/2-self.__counter.get_width()/2,self.__win.get_height()/2+40))
                if 1400 < self.__timer -  self.__ball.getTimer() < 2100:
                    self.__counter = self.__font.render('1',True,(171,178,191))
                    self.__win.blit(self.__counter,(self.__win.get_width()/2-self.__counter.get_width()/2,self.__win.get_height()/2+40))
            pygame.display.flip()
            self.__clock.tick(120)

if __name__ == '__main__':
    Game = Fenster()