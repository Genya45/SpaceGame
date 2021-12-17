#   Игра на пайтоне с использованием PyGame


import pygame
import random
from BulletClass import Bullet 
from UserShipClass import UserShip
from EnemyAsteroidClass import EnemyAsteroid
from math import sqrt
import random
import os

winWidth = 600
winHeight = 600
#WIN_WIDTH = 600
#WIN_HEIGHT = 600
ENEMY_ASTEROID_TICKS_MAX = 100
#FPS = int(1000/60)
FPS = 10
#clockFPS = pygame.time.Clock()

imageBackgroundSpaceNumber = None

isRunMainLoop = True

imageStarShip = None
imageBackgroundSpace = None




win = pygame.display.set_mode((winWidth,winHeight), pygame.RESIZABLE | pygame.DOUBLEBUF | pygame.HWSURFACE)
pygame.display.set_caption("Cosmo Game")


bulletsList = []
enemyAsteroidList = []
enemyAsteroidTicks = 0
asteroidsListImages = []
userShip = UserShip(winWidth/2, winHeight-winHeight/3)

def getCountsImagesBackgroundSpace(pathImages):
    list = os.listdir(pathImages)
    return len(list)
    


def imageLoader():
    global imageStarShip
    global imageBackgroundSpace
    global imageBackgroundSpaceNumber
    global asteroidsListImages

    listImages = os.listdir("assets/images/asteroids")
    for num in range(1, len(listImages) + 1):
        asteroidImage = pygame.image.load('assets/images/asteroids/asteroid' + str(num) + '.jpg')
        asteroidImage.set_colorkey((255,255,255))
        asteroidImage = pygame.transform.scale(asteroidImage, (50,50))
        asteroidsListImages.append(asteroidImage)


    imageBackgroundSpaceNumber = random.randint(1,getCountsImagesBackgroundSpace("assets/images/backgrounds/"))

    imageStarShip = pygame.image.load('assets/images/starShipMain.png')
    #imageStarShip = pygame.transform.rotate(imageStarShip, 18)
    imageStarShip = pygame.transform.scale(imageStarShip, (userShip.width, userShip.height))
    imageStarShip.set_colorkey((255,255,255))
    imageBackgroundSpace = pygame.image.load('assets/images/backgrounds/backgroundSpace' + str(imageBackgroundSpaceNumber) + '.jpg')
    #imageBackgroundSpace = pygame.transform.scale(imageBackgroundSpace, win.get_size())


def enemyAsteroidUpdated():
    global enemyAsteroidTicks
    global asteroidsListImages
    enemyAsteroidTicks += 1

    

    if enemyAsteroidTicks >= ENEMY_ASTEROID_TICKS_MAX:
        enemyAsteroidTicks = 0
        numberImage = random.randint(1, len(asteroidsListImages)-1)
        enemyAsteroidList.append(EnemyAsteroid(winWidth, winHeight, asteroidsListImages[numberImage]))
        enemyAsteroidList[-1].image = pygame.transform.scale(enemyAsteroidList[-1].image, (enemyAsteroidList[-1].radius*2,enemyAsteroidList[-1].radius*2))

    for indexAsteroid, enemyAsteroid in enumerate(enemyAsteroidList):
        enemyAsteroid.update_position()        
        #pygame.draw.line(win, (0, 0, 255), (enemyAsteroid.posX, enemyAsteroid.posY), (userShip.posX + userShip.width/2, userShip.posY + userShip.height/2))
        #pygame.draw.circle(win, (255, 0, 255), (enemyAsteroid.posX, enemyAsteroid.posY), enemyAsteroid.radius )
        win.blit(enemyAsteroid.image, (enemyAsteroid.posX - enemyAsteroid.radius, enemyAsteroid.posY - enemyAsteroid.radius))

        for indexBull, bullet in enumerate(bulletsList):
            if sqrt((bullet.posX - enemyAsteroid.posX)**2 + (bullet.posY - enemyAsteroid.posY)**2) < (enemyAsteroid.radius + bullet.radius):
                bulletsList.pop(indexBull)
                enemyAsteroidList.pop(indexAsteroid)
                continue

        #Пример работы алгоритма.
        #https://math.semestr.ru/math/plot.php
        #\left(x-5\right)^2\ +\ \left(y-10\right)^2=4
        #\operatorname{abs}\left(x-5+y-10\right)\ +\operatorname{abs}\left(x\ -5-y+10\right)\ =\ 4
        #\left(x-1.5\right)^2+\left(y-11\right)^{2\ }=4
        #\operatorname{abs}\left(x-5+y-10\right)\ +\operatorname{abs}\left(x\ -5-y+10\right)\ =\ 4+4
        
        if (     enemyAsteroid.posX > (userShip.posX - enemyAsteroid.radius)) and \
                (enemyAsteroid.posX < (userShip.posX + userShip.width + enemyAsteroid.radius)) and \
                (enemyAsteroid.posY > (userShip.posY - enemyAsteroid.radius)) and \
                (enemyAsteroid.posY < (userShip.posY + userShip.height + enemyAsteroid.radius)):
            if len(enemyAsteroidList):
                enemyAsteroidList.pop(indexAsteroid)                
                continue
        
        if enemyAsteroid.isBorderOut():
            enemyAsteroidList.pop(indexAsteroid)
            continue
    

def keyTest():
    keys = pygame.key.get_pressed()
    if(keys[pygame.K_LEFT] or keys[pygame.K_a]):
        if userShip.posX > 0:
            userShip.posX -= userShip.speed
    if(keys[pygame.K_RIGHT] or keys[pygame.K_d]):
        if userShip.posX < winWidth - userShip.width:
            userShip.posX += userShip.speed
    if(keys[pygame.K_UP] or keys[pygame.K_w]):
        if userShip.posY > winHeight/2:
            userShip.posY -= userShip.speed
    if(keys[pygame.K_DOWN] or keys[pygame.K_s]):
        if userShip.posY < winHeight - userShip.height:
            userShip.posY += userShip.speed

def eventTest():
    global isRunMainLoop
    global winWidth
    global winHeight
    global imageBackgroundSpace
    for event in pygame.event.get():
        if event.type == pygame.VIDEORESIZE:    
            winWidth, winHeight = win.get_size()              
            imageBackgroundSpace = pygame.image.load('assets/images/backgrounds/backgroundSpace' + str(imageBackgroundSpaceNumber) + '.jpg')       
            #imageBackgroundSpace = pygame.transform.scale(imageBackgroundSpace, win.get_size())
        if event.type == pygame.QUIT:
            isRunMainLoop = False
            print("quit")
            break
        if event.type == pygame.KEYDOWN:                        
            if event.key == pygame.K_ESCAPE:
                isRunMainLoop = False
                print("quit")
                break
            if event.key == pygame.K_SPACE:
                if len(bulletsList) < userShip.maxCountBullets:
                    bulletsList.append(Bullet(userShip.posX + userShip.width / 2, userShip.posY-5, userShip.bulletSpeed))

def userBulletsUpdted():
    for indexBull, bullet in enumerate(bulletsList):
        bullet.update_position()
        pygame.draw.circle(win, (255,100,0), (bullet.posX, bullet.posY), bullet.radius )        
        #win.blit(bullet.image, (bullet.posX-25, bullet.posY-25))

        if bullet.posY < 0:
            bulletsList.pop(indexBull)

def userShipUpdted():
    win.blit(imageStarShip, (userShip.posX, userShip.posY))


imageLoader()

while isRunMainLoop:
    pygame.time.delay(FPS)
    #clockFPS.tick(FPS) 

    eventTest()            
    keyTest()

    win.fill((10, 0, 0))
    win.blit(imageBackgroundSpace, (0,0))
    enemyAsteroidUpdated()
    userBulletsUpdted()
    userShipUpdted()  
        
    pygame.display.update()


pygame.quit()