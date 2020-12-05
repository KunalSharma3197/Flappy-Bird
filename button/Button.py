# -*- coding: utf-8 -*-
# Utility for creating a button
import pygame
class Button() :
    def __init__(self, x, y, image, screen) :
        self.image = image
        self.screen = screen
        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]
        
    def draw(self) :
        # Get mouse position
        pos = pygame.mouse.get_pos()
        
        # Check if mouse is over the button
        if self.rect.collidepoint(pos) :
            if pygame.mouse.get_pressed()[0] == 1:
                return True
        # Draw button
        self.screen.blit(self.image, (self.rect.x, self.rect.y))
        return False
        
