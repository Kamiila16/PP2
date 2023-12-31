import pygame
import datetime

pygame.init()

WIDTH = 1400
HEIGHT = 1050

FPS = 60

t = datetime.datetime.now()
angle = -(int(t.strftime("%S")) * 6) - 6
angleM = -(int(t.strftime("%M")) * 6 + (int(t.strftime("%S")) * 6 / 60)) - 54
background = pygame.image.load('C:/Users/Админ/OneDrive/Рабочий стол/pp2 labs/lab9/img/mc.png')
second = pygame.image.load('C:/Users/Админ/OneDrive/Рабочий стол/pp2 labs/lab9/img/s.png')
minute = pygame.image.load('C:/Users/Админ/OneDrive/Рабочий стол/pp2 labs/lab9/img/h.png')
def rotate(image, rect, angle):
    new_image = pygame.transform.rotate(image, angle)
    rect = new_image.get_rect(center=rect.center)
    return new_image, rect
image = pygame.Surface((63, HEIGHT), pygame.SRCALPHA)
image.blit(second, (0, 0))  
orig_image = image
rect = image.get_rect(center=(WIDTH//2, HEIGHT//2))
imagem = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
imagem.blit(minute, (0, 0))
orig_imagem = imagem
rect1 = imagem.get_rect(center=(WIDTH//2, HEIGHT//2))
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MickeyClock")

finished = False
clock = pygame.time.Clock()

while not finished:
    clock.tick(FPS)  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
     
    screen.blit(background, (0, 0)) 
    screen.blit(image, rect)
    screen.blit(imagem, rect1)
    image, rect = rotate(orig_image, rect, angle)
    imagem, rect1 = rotate(orig_imagem, rect1, angleM)

    angle -= 0.099
    angleM -= 0.099 / 60
    
    pygame.display.flip()

pygame.quit()
    

