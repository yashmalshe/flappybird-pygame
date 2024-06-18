import pygame as pg
import random
import expy as ex

from sys import path
from sys import exit
import os

my_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(my_path)
path.append(my_path)

pg.init()
screen = pg.display.set_mode((800, 600))
clock = pg.time.Clock()

birdo = pg.Rect(50, 300, 75, 75)
pipe1 = pg.Rect(750, 0, 100, 200)
pipe2 = pg.Rect(750, 400, 100, 200)
start_button = pg.Rect(200, 0, 300, 100)
end_button = pg.Rect(200, 0, 300, 100)

bpipe = pg.image.load("toppipe.png")
bpipe = pg.transform.scale(bpipe, (pipe1[2], pipe1[3]))
tpipe = pg.transform.rotate(bpipe, 180)
birb = pg.image.load("birb.png")
birb = pg.transform.scale(birb, (75, 75))
bgimg = pg.image.load("Flappy Bird Background.jpg")
bgimg = pg.transform.scale(bgimg, (800, 600))

birdc = (219, 170, 60)
stbc = (150, 150, 150)
black = (0, 0, 0)
white = (207, 209, 159)
birdspeed = -7
birddown = 3
pipespeed = -6
state = 0
score = 0


def game():
    global state
    global score
    birddown = 3
    score = 0
    birdo = pg.Rect(50, 300, 75, 75)
    while state == 1:
        keys = pg.key.get_pressed()
        l, m, r = pg.mouse.get_pressed()
        Mx, My = pg.mouse.get_pos()

        pipe1[0] += pipespeed
        pipe2[0] += pipespeed

        birdo[1] += birddown

        if keys[pg.K_SPACE]:
            birdo[1] += birdspeed

        if pipe1[0] <= -75 and pipe2[0] <= -75:
            ran = random.randint(-150, 150)
            pipe1[1] = 400
            pipe2[1] = 0

            pipe1[1] += ran
            pipe2[1] += ran
            pipe1[0] = 875
            pipe2[0] = 875
            score += 1
            print(score)
        if (
            birdo.colliderect(pipe1)
            or birdo.colliderect(pipe2)
            or birdo[1] == 0
            or birdo[1] == 600
        ):
            pipe1[0] = 875
            pipe2[0] = 875
            stage = 2
            state = 2
        screen.blit(bgimg, (0, 0))
        screen.blit(tpipe, (pipe1[0], pipe1[1]))
        screen.blit(bpipe, (pipe2[0], pipe2[1]))
        screen.blit(birb, (birdo[0], birdo[1]))
        ex.printText(screen, white, score, 750, 0, 40)
        ex.printText(screen, white, "score:", 650, 0, 40)
        pg.event.pump()
        clock.tick(100)
        pg.display.flip()


def startmenu():
    global state
    global score
    while state == 0:
        pg.event.pump()

        l, m, r = pg.mouse.get_pressed()
        Mx, My = pg.mouse.get_pos()
        global birdo
        birdo[1] += birddown
        if birdo[1] <= 400:
            birdown = 2
        elif birdo[1] >= 200:
            birdown = -5
        if l == 1 and start_button.collidepoint(Mx, My) == True:
            state = 1
        pg.draw.rect(screen, stbc, start_button)
        ex.printText(screen, black, "start", 300, 0, 50)
        pg.display.flip()
        screen.blit(bgimg, (0, 0))
        screen.blit(birb, (birdo[0], birdo[1]))


def retry():
    global state
    global score
    while state == 2:
        pg.event.pump()

        l, m, r = pg.mouse.get_pressed()
        Mx, My = pg.mouse.get_pos()

        if l == 1 and start_button.collidepoint(Mx, My) == True:
            state = 1

        screen.fill(white)
        pg.draw.rect(screen, stbc, end_button)
        ex.printText(screen, black, "retry", 300, 0, 50)
        pg.draw.rect(screen, stbc, (200, 100, 300, 50))
        ex.printText(screen, black, "your score was", 210, 100, 40)
        ex.printText(screen, black, score, 460, 100, 40)
        pg.display.flip()


while True:
    state = 0
    if state == 0:
        startmenu()
    if state == 1:
        game()
    if state == 2:
        retry()
    clock.tick(100)
