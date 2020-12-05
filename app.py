# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
from bird.Bird import Bird 
from pipe.Pipe import Pipe
from button.Button import Button
import random

pygame.init()

clock = pygame.time.Clock()
fps = 60
# Window dimensions of the app
screen_width = 864
screen_height = 665
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Flappy Bird')

# Define font
font = pygame.font.SysFont('Bauhaus 93', 60)

# Define color
white = (255, 255, 255)

# Define game variables
ground_scroll = 0
scroll_speed = 4
pipe_gap = 150
pipe_frequency = 1500 # miliseconds
last_pipe = pygame.time.get_ticks() - pipe_frequency
flappy = Bird(100, int(screen_height / 2), False, False) #  Bird(x, y, flying, game_over)
score = 0
pass_pipe = False

# Load images
bg = pygame.image.load('images/bg.jpg')
ground = pygame.image.load('images/ground.png')
restart_img = pygame.image.load('images/restart.png')

# Draw text
def draw_text(text, font, color, x, y) :
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

# Reset game
def reset_game() :
    pipe_group.empty()
    flappy.rect.x = 100
    flappy.rect.y = int(screen_height / 2)
    score = 0
    return score


bird_group = pygame.sprite.Group()
bird_group.add(flappy)
pipe_group = pygame.sprite.Group()

# Create a restart button
restart_button = Button(screen_width // 2 - 50, screen_height // 2 - 100, restart_img, screen)

run = True # represents state of the game
while run == True :
    clock.tick(fps)
    # Draw the backgroud
    screen.blit(bg, (0, 0))
    bird_group.draw(screen)
    bird_group.update()
    pipe_group.draw(screen)
    
    # Draw the ground
    screen.blit(ground, (ground_scroll, 576))
    
    # Check the score 
    if len(pipe_group) > 0 :
        if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.left\
            and bird_group.sprites()[0].rect.right < pipe_group.sprites()[0].rect.right\
            and pass_pipe == False :
            pass_pipe = True
        if pass_pipe == True :
            if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.right :
                score += 1
                pass_pipe = False
                
    # Show the score
    draw_text(str(score), font, white, int(screen_width / 2), 20)
    
    # Check for collisions
    if pygame.sprite.groupcollide(bird_group, pipe_group, False, False)  or flappy.rect.top < 0:
        flappy.game_over = True
 
    if flappy.rect.bottom >= 576:
        flappy.game_over = True
        flappy.flying = False
        
    if flappy.game_over == False and flappy.flying == True:
        # Generate pipes
        time_now = pygame.time.get_ticks()
        if time_now - last_pipe > pipe_frequency :
            pipe_height = random.randint(-100, 100)
            btm_pipe = Pipe(screen_width, int(screen_height / 2) + pipe_height, -1, pipe_gap, scroll_speed)
            top_pipe = Pipe(screen_width, int(screen_height / 2) + pipe_height, 1, pipe_gap, scroll_speed)
            pipe_group.add(btm_pipe)
            pipe_group.add(top_pipe)
            last_pipe = time_now
            
            # Draw and Scroll the ground
        ground_scroll -= scroll_speed
        if abs(ground_scroll) > 35:
            ground_scroll = 0
        
        pipe_group.update()
        
    # Check for game_over and resetting the game
    if flappy.game_over == True :
        if restart_button.draw() == True :
            flappy.game_over = False
            score = reset_game()
            
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and flappy.flying == False and flappy.game_over == False :
            flappy.flying = True
            
    pygame.display.update()

pygame.quit()