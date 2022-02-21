import sys
from os import path
def resource_path(relative_path):
        if hasattr(sys, '_MEIPASS'):
            return path.join(sys._MEIPASS, relative_path)
        return path.join(path.abspath('.'), relative_path)
sys.path.append(resource_path('assets/scripts/'))
from start import *

if __name__ == "__main__":
    Game = Menu()
    Game.start()