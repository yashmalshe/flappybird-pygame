from pygame import event
from pygame import quit
from pygame import font
from pygame import QUIT

def printText(surface, colour, text, x, y, size = 25):

    calibri = font.SysFont('calibri', size)

    text = str(text) 
    label = calibri.render(text, False, colour)
    surface.blit(label,(x,y))

def check_exit():
    for e in event.get():
        if e.type == QUIT:
            quit()
            exit()



