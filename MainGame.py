#   Игра на пайтоне с использованием PyGame


import pygame
import random
from BulletClass import Bullet 
from UserShipClass import UserShip

WIN_WIDTH = 600
WIN_HEIGHT = 600
#FPS = int(1000/60)
FPS = 60
clockFPS = pygame.time.Clock()



userShip = UserShip(WIN_WIDTH/2, WIN_HEIGHT-WIN_HEIGHT/3)

run = True

imageStarShip = pygame.image.load('assets/images/starShipMain.png')
#imageStarShip = pygame.transform.rotate(imageStarShip, 18)
imageStarShip = pygame.transform.scale(imageStarShip, (50, 50))
imageStarShip.set_colorkey((255,255,255))
imageBackgroundSpace = pygame.image.load('assets/images/backgroundSpace.jpg')


win = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
pygame.display.set_caption("Cosmo Game")


bulletsList = []

while run:
    #pygame.time.delay(FPS)
    clockFPS.tick(60)
    

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False
            print("quit")
            break

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if len(bulletsList) < 10:
                    bulletsList.append(Bullet(userShip.posX + userShip.width / 2, userShip.posY))

    keys = pygame.key.get_pressed()
    if(keys[pygame.K_LEFT] or keys[pygame.K_a]):
        if userShip.posX > 0:
            userShip.posX -= userShip.speed
    if(keys[pygame.K_RIGHT] or keys[pygame.K_d]):
        if userShip.posX < WIN_WIDTH - userShip.width:
            userShip.posX += userShip.speed
    if(keys[pygame.K_UP] or keys[pygame.K_w]):
        if userShip.posY > WIN_HEIGHT/2:
            userShip.posY -= userShip.speed
    if(keys[pygame.K_DOWN] or keys[pygame.K_s]):
        if userShip.posY < WIN_HEIGHT - userShip.height:
            userShip.posY += userShip.speed





    #win.fill((5,0,10))
    win.blit(imageBackgroundSpace, (0,0))
    #pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    win.blit(imageStarShip, (userShip.posX, userShip.posY))
    #pygame.draw.circle(win, (255,0,0), (x-10, y-10), 5 )

    
    for indexBull, bullet in enumerate(bulletsList):
        bullet.update_position()
        pygame.draw.circle(win, (255,100,0), (bullet.posX, bullet.posY), bullet.radius )
        if bullet.posY < 0:
            bulletsList.pop(indexBull)
        
    pygame.display.update()






pygame.quit()