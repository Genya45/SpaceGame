import random
from BulletClass import Bullet 
from UserShipClass import UserShip
from EnemyAsteroidClass import EnemyAsteroid
from math import sqrt
import random
import os
import pygame

ENEMY_ASTEROID_TICKS_MAX = 100

class GameProcess():

    def __init__(self, win):

        self.win = win
        self.winWidth, self.winHeight = self.win.get_size()
        self.isRunMainLoop = True
        
        self.imageStarShip = None
        self.imageBackgroundSpace = None
        self.imageBackgroundSpaceNumber = None

        self.bulletsList = []
        self.enemyAsteroidList = []
        self.enemyAsteroidTicks = 0
        self.asteroidsListImages = []

        self.userShip = UserShip(self.winWidth/2, self.winHeight-self.winHeight/3)

        self.imageLoader()

    def getCountsImagesInDir(self, pathImages):
        list = os.listdir(pathImages)
        return len(list)  

    def imageLoader(self):
        countImagesAsteroids = self.getCountsImagesInDir("assets/images/asteroids")
        for num in range(1, countImagesAsteroids + 1):
            self.asteroidImage = pygame.image.load('assets/images/asteroids/asteroid' + str(num) + '.jpg')
            self.asteroidImage.set_colorkey((255,255,255))
            #asteroidImage = pygame.transform.scale(asteroidImage, (50,50))
            self.asteroidsListImages.append(self.asteroidImage)


        self.imageBackgroundSpaceNumber = random.randint(1, self.getCountsImagesInDir("assets/images/backgrounds/"))

        self.imageStarShip = pygame.image.load('assets/images/starShipMain.png')
        #imageStarShip = pygame.transform.rotate(imageStarShip, 18)
        self.imageStarShip = pygame.transform.scale(self.imageStarShip, (self.userShip.width, self.userShip.height))
        self.imageStarShip.set_colorkey((255,255,255))
        self.imageBackgroundSpace = pygame.image.load('assets/images/backgrounds/backgroundSpace' + str(self.imageBackgroundSpaceNumber) + '.jpg')
        #imageBackgroundSpace = pygame.transform.scale(imageBackgroundSpace, win.get_size())


    def enemyAsteroidUpdated(self):
        self.enemyAsteroidTicks += 1

        

        if self.enemyAsteroidTicks >= ENEMY_ASTEROID_TICKS_MAX:
            self.enemyAsteroidTicks = 0
            numberImage = random.randint(1, len(self.asteroidsListImages)-1)
            self.enemyAsteroidList.append(EnemyAsteroid(self.winWidth, self.winHeight, self.asteroidsListImages[numberImage]))
            self.enemyAsteroidList[-1].image = pygame.transform.scale(self.enemyAsteroidList[-1].image, (self.enemyAsteroidList[-1].radius*2, self.enemyAsteroidList[-1].radius*2))

        for indexAsteroid, enemyAsteroid in enumerate(self.enemyAsteroidList):
            enemyAsteroid.update_position()        
            #pygame.draw.line(win, (0, 0, 255), (enemyAsteroid.posX, enemyAsteroid.posY), (userShip.posX + userShip.width/2, userShip.posY + userShip.height/2))
            #pygame.draw.circle(win, (255, 0, 255), (enemyAsteroid.posX, enemyAsteroid.posY), enemyAsteroid.radius )
            self.win.blit(enemyAsteroid.image, (enemyAsteroid.posX - enemyAsteroid.radius, enemyAsteroid.posY - enemyAsteroid.radius))

            for indexBull, bullet in enumerate(self.bulletsList):
                if sqrt((bullet.posX - enemyAsteroid.posX)**2 + (bullet.posY - enemyAsteroid.posY)**2) < (enemyAsteroid.radius + bullet.radius):
                    self.bulletsList.pop(indexBull)
                    self.enemyAsteroidList.pop(indexAsteroid)
                    continue

            #Пример работы алгоритма.
            #https://math.semestr.ru/math/plot.php
            #\left(x-5\right)^2\ +\ \left(y-10\right)^2=4
            #\operatorname{abs}\left(x-5+y-10\right)\ +\operatorname{abs}\left(x\ -5-y+10\right)\ =\ 4
            #\left(x-1.5\right)^2+\left(y-11\right)^{2\ }=4
            #\operatorname{abs}\left(x-5+y-10\right)\ +\operatorname{abs}\left(x\ -5-y+10\right)\ =\ 4+4
            
            if (     enemyAsteroid.posX > (self.userShip.posX - enemyAsteroid.radius)) and \
                    (enemyAsteroid.posX < (self.userShip.posX + self.userShip.width + enemyAsteroid.radius)) and \
                    (enemyAsteroid.posY > (self.userShip.posY - enemyAsteroid.radius)) and \
                    (enemyAsteroid.posY < (self.userShip.posY + self.userShip.height + enemyAsteroid.radius)):
                if len(self.enemyAsteroidList):
                    self.enemyAsteroidList.pop(indexAsteroid)                
                    continue
            
            if enemyAsteroid.isBorderOut():
                self.enemyAsteroidList.pop(indexAsteroid)
                continue
        
    def keyTest(self):
        keys = pygame.key.get_pressed()
        if(keys[pygame.K_LEFT] or keys[pygame.K_a]):
            if self.userShip.posX > 0:
                self.userShip.posX -= self.userShip.speed
        if(keys[pygame.K_RIGHT] or keys[pygame.K_d]):
            if self.userShip.posX < self.winWidth - self.userShip.width:
                self.userShip.posX += self.userShip.speed
        if(keys[pygame.K_UP] or keys[pygame.K_w]):
            if self.userShip.posY > self.winHeight/2:
                self.userShip.posY -= self.userShip.speed
        if(keys[pygame.K_DOWN] or keys[pygame.K_s]):
            if self.userShip.posY < self.winHeight - self.userShip.height:
                self.userShip.posY += self.userShip.speed

    def eventTest(self):
        for event in pygame.event.get():
            if event.type == pygame.VIDEORESIZE:    
                self.winWidth, self.winHeight = self.win.get_size()              
                self.imageBackgroundSpace = pygame.image.load('assets/images/backgrounds/backgroundSpace' + str(self.imageBackgroundSpaceNumber) + '.jpg')       
                #imageBackgroundSpace = pygame.transform.scale(imageBackgroundSpace, win.get_size())
            if event.type == pygame.QUIT:
                self.isRunMainLoop = False
                print("quit")
                break
            if event.type == pygame.KEYDOWN:                        
                if event.key == pygame.K_ESCAPE:
                    self.isRunMainLoop = False
                    print("quit")
                    break
                if event.key == pygame.K_SPACE:
                    if len(self.bulletsList) < self.userShip.maxCountBullets:
                        self.bulletsList.append(Bullet(self.userShip.posX + self.userShip.width / 2, self.userShip.posY-5, self.userShip.bulletSpeed))

    def userBulletsUpdted(self):
        for indexBull, bullet in enumerate(self.bulletsList):
            bullet.update_position()
            pygame.draw.circle(self.win, (255,100,0), (bullet.posX, bullet.posY), bullet.radius )        
            #win.blit(bullet.image, (bullet.posX-25, bullet.posY-25))

            if bullet.posY < 0:
                self.bulletsList.pop(indexBull)






    def userShipUpdted(self):
        self.win.blit(self.imageStarShip, (self.userShip.posX, self.userShip.posY))


    def updateDisplay(self):
        self.win.fill((10, 0, 0))
        self.win.blit(self.imageBackgroundSpace, (0,0))
        self.enemyAsteroidUpdated()
        self.userBulletsUpdted()
        self.userShipUpdted()          
        pygame.display.update()


