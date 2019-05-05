import pygame
import sys
import math
import random
from threading import Timer
from TargetOne import TargetOne
from Car import Car
from pTimer import pTimer
from ScoreBoard import ScoreBoard

class ChapterOne():
    def __init__(self, screen):
        self.name = "Let's Start"
        self.car = Car(screen)
        self.targets = []
        self.backGroundImage = pygame.transform.scale(pygame.image.load("images/png/arkaplan.png"),
                                                      (screen.get_width(), screen.get_height()))
        self.backGroundImageX = 0
        self.backGroundImageY = 0
        self.screen = screen
        self.xx = 0
        # 2 saniyede bir hedef üretilmeli
        # bunun için kendi yazdığımız timer sınıfını kulllıyoruz
        # bu işlem için uygun olan threadlerdir ancak bu konuya sonra geleceğiz
        self.pgenerateTargetTimer = pTimer(2, self.generateTarget, screen)

        self.finishEvent = pygame.event.Event(pygame.USEREVENT, attr1='finishEvent')

    def start(self, screen):

        self.pgenerateTargetTimer.start()

    def finish(self, screen):
        self.pgenerateTargetTimer.stop()
        pygame.event.post(self.finishEvent)

    def generateTarget(self, arguments):
        newTarget = TargetOne(arguments[0])
        self.targets.append(newTarget)
        

    def drawBackGround(self, screen):
        screen.blit(self.backGroundImage, ( 0,self.backGroundImageX))
        self.backGroundImageX = self.backGroundImageX + 1
        screen.blit(self.backGroundImage, ( 0, self.backGroundImageX - screen.get_width() ))
        # resim dönüşünde x değerini sıfırlıyoruz
        
        if screen.get_width() == +self.backGroundImageX:
            self.backGroundImageX = 0

    def drawPlane(self, screen):
        self.car.draw(screen)
        

    def drawTargets(self, screen):
        
        for target in self.targets:
            exposed = target.draw(screen)
            if exposed:
                self.targets.remove(target)
                
                if self.car.exposed:
                    pygame.event.post(self.car.exposedEvent)
                    self.finish(screen)

            else:
                if target.rectangle.colliderect(self.car.rectangle):
                    
                    if not target.exposed:
                        
                        target.expose()
                        self.car.expose()
            
                
    
    def draw(self, screen):
        self.drawBackGround(screen)
        self.drawPlane(screen)
        self.drawTargets(screen)
