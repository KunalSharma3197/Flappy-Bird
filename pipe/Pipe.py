# -*- coding: utf-8 -*-
# Pipes represent obstacles in the game
import pygame
from pygame.locals import *

class Pipe(pygame.sprite.Sprite) :
    def __init__(self, x, y, position, pipe_gap, scroll_speed) :
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('./images/pipe.png')
        self.rect = self.image.get_rect()
        self.position = position
        self.pipe_gap = pipe_gap
        self.scroll_speed = scroll_speed
        # position 1 means from the top, -1 means from the bottom
        if self.position == 1 :
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x, y - int(self.pipe_gap / 2)]
        if self.position == -1 :
            self.rect.topleft = [x, y + int(pipe_gap / 2)]
        
    def update(self) :
        self.rect.x -= self.scroll_speed
        if self.rect.right < 0 :
            self.kill()
