import pygame
import sys
import math
import random



class Car():
    def __init__(self, screen):
        self.x = 0
        self.y = 0
        self.mx = 0  # x haraket yönü
        self.my = 0  # x haraket yönü
        width = screen.get_width()
        height = screen.get_height()
        self.rectangle = pygame.rect.Rect(370, int(height / 1) - int(height / 5 / 2), int(width / 17), int(height / 10))
        self.flyImageOrder = 0
        self.flyImages = [pygame.transform.scale(pygame.image.load("images/png/car1.png"),
                                                 (self.rectangle[2], self.rectangle[3])),
                          pygame.transform.scale(pygame.image.load("images/png/car1.png"),
                                                 (self.rectangle[2], self.rectangle[3]))]


        


        self.exposed = False
        self.exposedEvent = pygame.event.Event(pygame.USEREVENT, attr1='planeExposedEvent')

    def draw(self, screen):
        self.rectangle[0] = self.rectangle[0] + self.mx * 2
        self.rectangle[1] = self.rectangle[1] + self.my * 2
        self.rectangle.clamp_ip(screen.get_rect())  # plane objesini ekran karesi içinde tutar
        screen.blit(self.flyImages[self.flyImageOrder], self.rectangle)
        
        
        
        

    def expose(self):
        
        self.exposed = True

    


