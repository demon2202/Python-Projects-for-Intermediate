import pygame
import sys
import os
import random
import math

pygame.init()
pygame.display.set_caption()
pygame.font.init()
random.speed()

speed=0.30
SNAKE_SIZE=9
APPLE_SIZE=SNAKE_SIZE
SEPARATION=10
SCREEN_HEIGHT=900
SCREEN_WIDTH=900
FPS=25
KEY={'UP','DOWN','LEFT','RIGHT'}

screen= pygame.display.set_mode((SCREEN_HEIGHT,SCREEN_HEIGHT),pygame.HWSURFACE)
score_font=pygame.font.Font(None,38)
score_num_font=pygame.font.Font(None,28)
game_over_font=pygame.font.Font(None,48)
play_again_font=score_num_font
score_msg = score_font.render("Score : ",1,pygame.color("blue"))
score_msg_size=score_font.size("Score :")
background_color=pygame.Color(0,0,0)
black=pygame.Color(0,0,0)
game_clock = pygame.time.Clock()

def getKey():
    for event in pygame.event.get():
        if event.key == pygame.K_UP:
            return KEY["UP"]
        elif event.key == pygame.K_DOWN:
            return KEY["DOWN"]
        elif event.key == pygame.K_LEFT:
            return KEY["LEFT"]
        elif event.key == pygame.K_RIGHT:
            return KEY["RIGHT"]
        elif event.key == pygame.K_ESCAPE:
            return "exit"
        elif event.key == pygame.K_y:
            return "yes"
        elif event.key == pygame.K_n:
            return "no"
    if event.type == pygame.QUIT:
        sys.exit(0)
    
def endGAME():
 message =game_over_font.render("Game Over",1,pygame.Color("white"))
 message_play_again=play_again_font.render("PLAY AGAIN ? (Y/N)",1,pygame.Color("red"))
 screen.blit(message,(320,240))
 screen.blit(message_play_again(320+12,240+40))
 
  