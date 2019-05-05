import pygame
import sys
import math
import random
from ScoreBoard import ScoreBoard

class TargetOne():
    def __init__(self, screen):
        self.x = 0
        self.y = 0
        self.mx =  0# x haraket yönü
        self.my = 1# y haraket yönü
        self.life = 100
        self.hiz = 2
        width = screen.get_width()
        height = screen.get_height()
        self.x = random.randint(213, 550)
        self.rectangle = pygame.rect.Rect(self.x,0, int(width / 20),
                                          int(height / 10))
        

        self.flyImageOrder = 0
        self.flyImages = []
        for i in range(1, 11):
            self.flyImages.append(
                pygame.transform.scale(pygame.image.load("images/png/car2.png"),
                                       (self.rectangle[2], self.rectangle[3])))

        self.explosionImageOrder = -1
        self.explosionImages = []
        for i in range(1, 10):
            self.explosionImages.append(
                pygame.transform.scale(pygame.image.load("images/png/crash.png"),
                                       (self.rectangle[2] * 4, self.rectangle[2] * 4)))
        self.exposed = False

    
   
    
    def draw(self, screen):
        if self.explosionImageOrder == -1:
            self.flyImageOrder = (self.flyImageOrder + 1) % 10
            # self.rectangle[0]=self.rectangle[0]-self.mx*2
            self.rectangle[1] = self.rectangle[1] + self.my * self.hiz
            # self.rectangle.centerx= self.rectangle.centerx-self.mx*2
            screen.blit(self.flyImages[self.flyImageOrder],
                        [self.x,
                         self.rectangle[1] - int(self.flyImages[self.flyImageOrder].get_height() / 2) ])

        else:
            self.explosionImageOrder = (self.explosionImageOrder + 1) % 9
            #self.rectangle[0] = self.rectangle[0] + self.mx * 2
            self.rectangle[1] = self.rectangle[1] + self.my * self.hiz
            #self.rectangle.centerx = self.rectangle.centerx + self.mx * 2
            #self.rectangle.centery = self.rectangle.centery + self.my * 2
            if self.explosionImageOrder == 8:
                return True

            screen.blit(self.explosionImages[self.explosionImageOrder],
                        [self.x,
                         self.rectangle[1]-  int(self.explosionImages[self.explosionImageOrder].get_height() / 2)])
            
            if self.explosionImageOrder == 8:
                self.explosionImageOrder = -1

        return False

    
    def expose(self):
        
        self.life=0
        self.exposed=True
        if self.explosionImageOrder<0:
            self.explosionImageOrder=0


    def hizDonder(self,hiz):
        hiz = hiz+2
        return hiz