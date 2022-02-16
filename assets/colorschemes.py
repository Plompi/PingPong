import json

class colorschemes:
    def __init__(self):
        #name, backgroundcolor, textcolor, accentcolor, ballcolor
        self.__colors =(    ['Bushido',"#242933","#596172","#ec4c56","#d1d0c5"],
                            ["SerikaDark","#323437","#646669","#e2b714","#d1d0c5"],
                            ["Dev","#1b2028","#4b5975","#23a9d5","#d1d0c5"],
                            ["Trackday","#464d66","#5c7eb9","#e0513e","#d1d0c5"],
                            ["Alpine","#6c687f","#9994b8","#ffffff","#d1d0c5"],
                            ["Bento","#2d394d","#4a768d","#ff7a90","#d1d0c5"],
                            ["IcebergDark","#161821","#c6c8d1","#84a0c6","#d1d0c5"],
                            ["EvilEye","#0084c2","#01589f","#f7f2ea","#d1d0c5"],
                            ["Nautilus","#132237","#1cbaac","#ebb723","#d1d0c5"]

                    
                    
                    
                    
                    
                    
        )

    def hex_to_rgb(self,hexcolor):
        return tuple(int(hexcolor[1:][i:i+2], 16) for i in (0, 2, 4))

    def setactivecolor(self,index):
        with open('selected_scheme.json','w') as theme:
            json.dump(self.__colors[index],theme)

    def loadactivecolor(self):
        try:
            with open('selected_scheme.json') as theme:
                self.__loaded = json.load(theme)
            return self.__loaded
        except:
            with open('selected_scheme.json','w') as theme:
                json.dump(self.__colors[0],theme)
            return self.__colors[0]

    def indexofcolor(self,color):
        return self.__colors.index(color)

    def allcolors(self):
        return self.__colors