#çizim ile işlemler yapabilsek dahi kontrol için objelere ihtiyacımız vardır.
#bu noktada object merkezli programlama yapmamız gerekir.
import pygame
import sys
import math
import random
from Chapter import ChapterOne
from TargetOne import  TargetOne
from Menu import Menu
from ScoreBoard import ScoreBoard
pygame.init()

gameDisplay_width=800
gameDisplay_height=800
gameDisplay = pygame.display.set_mode((gameDisplay_width,gameDisplay_height))
pygame.display.set_caption('Gamemaker')

crashed = False
deneme = 0
clock = pygame.time.Clock()
chapter= ChapterOne(gameDisplay)
chapter.start(gameDisplay)
endEvent=pygame.event.Event(pygame.USEREVENT, attr1='endEvent')
menu = Menu(gameDisplay.get_rect())
end=False
ScoreBoard.init_ScoreBoard()
ScoreBoard.set_Fuel()
ScoreBoard.set_Score()
while not crashed:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            crashed = True
        elif event.type == pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                chapter.pgenerateTargetTimer.pause(True)
                crashed=menu.runMenu(gameDisplay)
                chapter.pgenerateTargetTimer.pause(False)
            if event.key == pygame.K_UP:
                chapter.car.my=-1
            if event.key == pygame.K_DOWN:
                chapter.car.my=1
            if event.key == pygame.K_LEFT:
                chapter.car.mx=-1
            if event.key == pygame.K_RIGHT:
                chapter.car.mx=1
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                chapter.car.my=0
            if event.key == pygame.K_DOWN:
                chapter.car.my=0
            if event.key == pygame.K_LEFT:
                chapter.car.mx=0
            if event.key == pygame.K_RIGHT:
                chapter.car.mx=0
        #event karşılaştırmalarında eşitlik koşulu çalışır
        #eventlar aynı olmalı özellikleriyle birlikte
        elif event== chapter.finishEvent:
            print(event)
            end=True

        elif event== chapter.car.exposedEvent:
            print(event)
    if not end:
        chapter.draw(gameDisplay)
        ScoreBoard.draw(gameDisplay)
        deneme = deneme + 1
        if deneme%100 == 0:
            ScoreBoard.set_Fuel(100)
        ScoreBoard.set_Score(1)


    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()

