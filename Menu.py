from Button import *
from CouchMain import *

class Menu:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('PingPong')
        self.__win = pygame.display.set_mode((933,700))
        self.__clock = pygame.time.Clock()
        self.__selected = 1
        self.__buttons = [
            Button('PINGPONG',70,(self.__win.get_width()/2,self.__win.get_height()/2-300),(255,255,255),False),
            Button('COUCH',70,(self.__win.get_width()/2,self.__win.get_height()/2-80),(255,255,120),True),
            Button('LOCAL',70,(self.__win.get_width()/2,self.__win.get_height()/2),(255,255,255),False),
            Button('QUIT',70,(self.__win.get_width()/2,self.__win.get_height()/2+80),(255,255,255),False)
        ]

        while True:
            for event in pygame.event.get():
                self.__keys = pygame.key.get_pressed()
                if self.__keys[pygame.K_ESCAPE] or event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if ((self.__keys[pygame.K_w] or self.__keys[pygame.K_UP]) and self.__selected != 1) and event.type == pygame.KEYDOWN:
                            self.__buttons[self.__selected-1].setSelected(True)
                            self.__buttons[self.__selected].setSelected(False)
                            self.__selected -=1

                if ((self.__keys[pygame.K_s] or self.__keys[pygame.K_DOWN]) and self.__selected != 3) and event.type == pygame.KEYDOWN:
                            self.__buttons[self.__selected+1].setSelected(True)
                            self.__buttons[self.__selected].setSelected(False)
                            self.__selected +=1

                if self.__keys[pygame.K_RETURN] and event.type == pygame.KEYDOWN:
                    if self.__selected == 1:
                        Fenster(self.__win)
                    if self.__selected == 3:
                        pygame.quit()
                        exit()
                
            self.__win.fill((40, 44, 52))
            for i in self.__buttons:
                self.__win.blit(i.Buttonreturn()[0],(i.position()[0],i.position()[1]))
            pygame.display.flip()
            self.__clock.tick(120)

menu = Menu()