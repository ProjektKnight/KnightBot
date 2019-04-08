import pygame
import os
window = pygame.display.set_mode((550,550))
#spirites = pygame.sprite.Group()
#help(pygame.draw.r)
#while True:
#    pygame.draw.rect(window,(255,255,255),(10,20,40,60),50)
#global s
#s=0
#print(s)
#if not (play.isdjump):  # checks whether the variable is filled with none,empty,zero or False and if yes then it will execute
 #   if keys[pygame.K_KP_ENTER]:
 #       isdjump = True
 #       walkleft = False
 #       walkright = False
 #       wcount = 0
#else:
 #   if jumpcount >= -10:
 #       y -= (jumpcount ** 2) * 0.5
 #       jumpcount -= 1
 #   elif djumpcount <= 12:
 #       y -= (djumpcount ** 2) * 0.5 * -1
 #       djumpcount += 1
 #   else:
 #      y += 60
 #       isdjump = False
 #       djumpcount = 0
 #       jumpcount = 10
def game(run):
    play = players(30, 250, 50, 50)
    ghost = Ghostplay(60, 250, 50, 50, 300)
    bullets = []
    window = pygame.display.set_mode((405, 304))
    time.sleep(5)