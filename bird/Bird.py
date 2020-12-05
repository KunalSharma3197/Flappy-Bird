# -*- coding: utf-8 -*-
# Class representing bird in the game
import pygame
from pygame.locals import *

class Bird(pygame.sprite.Sprite) :
    def __init__(self, x, y, flying, game_over) :
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        for i in range(1, 4) :
            img = pygame.image.load(f"./images/bird{i}.png")
            self.images.append(img)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.vel = 0
        self.clicked = False
        self.flying = flying
        self.game_over = game_over
    
    def update(self) :
        if self.flying == True :
            # Applying gravity
            self.vel += 0.5
            if self.vel > 8 :
                self.vel = 8
#            print(self.vel)
            if self.rect.bottom < 576 :
                self.rect.y += int(self.vel)
        # Jump on mouse clicks
        if self.game_over == False :
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False :
                self.clicked = True
                self.vel = -10
            if pygame.mouse.get_pressed()[0] == 0 and self.clicked == True :
                self.clicked = False
                
            # Handle animation
            self.counter += 1
            flap_cooldown = 5
            if self.counter > flap_cooldown :
                self.counter = 0
                self.index += 1
                if self.index == len(self.images) :
                    self.index = 0
                self.image = self.images[self.index]
                
            # Rotate the bird 
            self.image = pygame.transform.rotate(self.images[self.index], self.vel * -2)
        else :
            self.image = pygame.transform.rotate(self.images[self.index], -90)
            