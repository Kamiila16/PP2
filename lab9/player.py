import pygame 
import os
import sys

pygame.init()
screen = pygame.display.set_mode((800,200))
pygame.display.set_caption("fav")
red = (255, 0, 0)
black = (0, 0, 0)
font=pygame.font.SysFont(None, 70)
lybrary = ['C:/Users/Админ/OneDrive/Рабочий стол/pp2 labs/lab9/music/1.mp3', 
           'C:/Users/Админ/OneDrive/Рабочий стол/pp2 labs/lab9/music/2.mp3', 
           'C:/Users/Админ/OneDrive/Рабочий стол/pp2 labs/lab9/music/3.mp3']
ctrack = 0
running = True
running_song = True

def start_music(track):
    pygame.mixer.music.load(lybrary[track])
    pygame.mixer.music.play()

def play_music(running_song):
    if running_song:
        pygame.mixer.music.unpause()
    else:
        pygame.mixer.music.pause()

start_music(ctrack)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                running_song = not running_song
                play_music(running_song)
            elif event.key==pygame.K_RIGHT:
                ctrack+=1
                if ctrack==len(lybrary):
                    ctrack=0
                start_music(ctrack)
            elif event.key==pygame.K_LEFT:
                ctrack-=1
                if ctrack<0:
                    ctrack=len(lybrary)-1
                start_music(ctrack)
               

   
    text=font.render("Best songs", True, red)
    screen.blit(text, (10,10))
    pygame.display.flip()

pygame.quit()
