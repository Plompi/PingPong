import sys
from button import *
from colorschemes import *

class Gameover:
    def __init__(self,scheme,win,winner,menu):
        pygame.mixer.music.stop()
        self.__button_sound = pygame.mixer.Sound("assets/sounds/button.wav")
        self.__button_sound.set_volume(0.2)
        self.__menu = menu
        self.__winner = winner
        self.__scheme = scheme
        self.__color = self.__scheme.loadactivecolor()[1]
        self.__win = win
        self.__clock = pygame.time.Clock()
        self.__selected = 1
        self.__buttons = [
            Button(f'{self.__winner} WON!',100,(self.__win.get_width()/2,self.__win.get_height()/2-300),self.__scheme,self.__win,1),
            Button('RESTART',100,(self.__win.get_width()/2,self.__win.get_height()/2-80),self.__scheme,self.__win,-1),
            Button('MENU',100,(self.__win.get_width()/2,self.__win.get_height()/2),self.__scheme,self.__win,1),
            Button('QUIT',100,(self.__win.get_width()/2,self.__win.get_height()/2+80),self.__scheme,self.__win,1)
        ]

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

                    if event.key == pygame.K_RETURN:
                        if self.__selected == 1:
                            pygame.mixer.music.play(-1)
                            return

                        if self.__selected == 2:
                            pygame.mixer.music.load("assets/sounds/menu.wav")
                            pygame.mixer.music.play(-1)
                            pygame.mixer.music.set_volume(0.1)
                            self.__menu.start()

                        if self.__selected == 3:
                            pygame.quit()
                            sys.exit()

            self.__win.fill(self.__color)

            for i in self.__buttons:
                i.draw()
            pygame.display.flip()
            self.__clock.tick(120)