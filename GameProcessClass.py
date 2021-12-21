import random
from BulletClass import Bullet 
from UserShipClass import UserShip
from EnemyAsteroidClass import EnemyAsteroid
from math import sqrt
import random
import os
import pygame


class GameProcess():
    

    def __init__(self, win):

        self.win = win
        self.winWidth, self.winHeight = self.win.get_size()
        self.isRunMainLoop = True
        
        self.imageStarShipList = []
        self.imageBackgroundSpace = None
        self.imageBackgroundSpaceNumber = None
        self.userBulletImagesList = []        
        self.enemyAsteroidBoomImagesList = []

        self.imagePathAsteroids = "assets/images/asteroids/"
        self.imagePathAsteroidsBoom = "assets/images/asteroidsBoom/"
        self.imagePathBackgroundSpace = "assets/images/backgrounds/"
        self.imagePathStarShip = "assets/images/userStarShips/"
        self.imagePathUserBullet = "assets/images/userBullets/"

        self.bulletsList = []
        self.enemyAsteroidTicks = 0
        self.enemyAsteroidList = []
        self.asteroidsListImages = []
        
        self.backgroundTimeTick = 0
        self.backgroundTimeTickMax = 10
        self.backgroundPosition = 0

        self.enemyAsteroidTicksMax = 100

        self.userShip = UserShip(self.winWidth/2, self.winHeight-self.winHeight/3, self.winWidth, self.winHeight)


        self.imageLoader()


    def imageLoader(self):
        for imageAsteroid in os.listdir(self.imagePathAsteroids):       
            asteroidImage = pygame.image.load(self.imagePathAsteroids + imageAsteroid)
            #asteroidImage = pygame.transform.scale(asteroidImage, (50,50))
            self.asteroidsListImages.append(asteroidImage)
        
        for imageAteroidBoom in os.listdir(self.imagePathAsteroidsBoom):
            imageBoom = pygame.image.load(self.imagePathAsteroidsBoom + imageAteroidBoom)
            self.enemyAsteroidBoomImagesList.append(imageBoom)
        
        for imageStarship in os.listdir(self.imagePathStarShip):
            imgStarship = pygame.image.load(self.imagePathStarShip + imageStarship)
            imgStarship = pygame.transform.scale(imgStarship, (self.userShip.width, self.userShip.height))
            self.imageStarShipList.append(imgStarship)
        self.userShip.imageList = self.imageStarShipList


        listImagesBackgroundSpace = os.listdir(self.imagePathBackgroundSpace)
        self.imageBackgroundSpaceNumber = random.randint(0, len(listImagesBackgroundSpace) - 1)
        self.imageBackgroundSpace = pygame.image.load(self.imagePathBackgroundSpace + listImagesBackgroundSpace[self.imageBackgroundSpaceNumber])
        self.imageBackgroundSpace = pygame.transform.scale(self.imageBackgroundSpace, self.win.get_size())


        for imageBullet in os.listdir(self.imagePathUserBullet):
            image = pygame.image.load(self.imagePathUserBullet + imageBullet)
            #image = pygame.transform.scale(image, (20,20))
            self.userBulletImagesList.append(image)
        






    def enemyAsteroidUpdated(self):
        self.enemyAsteroidTicks += 1

        

        if self.enemyAsteroidTicks >= self.enemyAsteroidTicksMax:
            self.enemyAsteroidTicks = 0
            numberImage = random.randint(1, len(self.asteroidsListImages)-1)
            self.enemyAsteroidList.append(EnemyAsteroid(self.winWidth, self.winHeight, self.asteroidsListImages[numberImage], self.enemyAsteroidBoomImagesList.copy()) )
            self.enemyAsteroidList[-1].image = pygame.transform.scale(self.enemyAsteroidList[-1].image, (self.enemyAsteroidList[-1].radius*2, self.enemyAsteroidList[-1].radius*2))
            for i in range(0, len(self.enemyAsteroidBoomImagesList)):
                self.enemyAsteroidList[-1].imageBoomList[i] = pygame.transform.scale(self.enemyAsteroidList[-1].imageBoomList[i], (self.enemyAsteroidList[-1].radius*2, self.enemyAsteroidList[-1].radius*2))

        for indexAsteroid, enemyAsteroid in enumerate(self.enemyAsteroidList):
            enemyAsteroid.update_position()        
            #pygame.draw.line(win, (0, 0, 255), (enemyAsteroid.posX, enemyAsteroid.posY), (userShip.posX + userShip.width/2, userShip.posY + userShip.height/2))
            #pygame.draw.circle(win, (255, 0, 255), (enemyAsteroid.posX, enemyAsteroid.posY), enemyAsteroid.radius )
            self.win.blit(enemyAsteroid.image, (enemyAsteroid.posX - enemyAsteroid.radius, enemyAsteroid.posY - enemyAsteroid.radius))

            if not enemyAsteroid.isBoom:
                for indexBull, bullet in enumerate(self.bulletsList):
                    if sqrt((bullet.posX - enemyAsteroid.posX)**2 + (bullet.posY - enemyAsteroid.posY)**2) < (enemyAsteroid.radius + bullet.radius):
                        self.bulletsList.pop(indexBull)
                        #self.enemyAsteroidList.pop(indexAsteroid)
                        enemyAsteroid.isBoom = True
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
            
            if enemyAsteroid.isBorderOut() and len(self.enemyAsteroidList):
                self.enemyAsteroidList.pop(indexAsteroid)
                continue

            if enemyAsteroid.isDead and len(self.enemyAsteroidList):
                self.enemyAsteroidList.pop(indexAsteroid)
                continue

        
    def keyTest(self):        
        self.userShip.change_direction(0)
        keys = pygame.key.get_pressed()
        if(keys[pygame.K_RIGHT] or keys[pygame.K_d]):            
            self.userShip.change_direction(1)
        if(keys[pygame.K_LEFT] or keys[pygame.K_a]):
            self.userShip.change_direction(-1)
        if(keys[pygame.K_UP] or keys[pygame.K_w]):
            self.userShip.change_direction(2)
        if(keys[pygame.K_DOWN] or keys[pygame.K_s]):
            self.userShip.change_direction(-2)

    def eventTest(self):
        for event in pygame.event.get():
            if event.type == pygame.VIDEORESIZE:    
                self.winWidth, self.winHeight = self.win.get_size()  
                self.userShip.maxW, self.userShip.maxH = self.winWidth, self.winHeight   
                self.imageBackgroundSpace = pygame.image.load(self.imagePathBackgroundSpace + os.listdir(self.imagePathBackgroundSpace)[self.imageBackgroundSpaceNumber])               
                self.imageBackgroundSpace = pygame.transform.scale(self.imageBackgroundSpace, self.win.get_size())

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
                        self.bulletsList.append(Bullet(self.userShip.posX + self.userShip.width / 2, self.userShip.posY-5, self.userBulletImagesList.copy(), self.userShip.bulletSpeed))

    def userBulletsUpdted(self):
        for indexBull, bullet in enumerate(self.bulletsList):
            bullet.update_position()
            #pygame.draw.circle(self.win, (255,100,0), (bullet.posX, bullet.posY), bullet.radius ) 
            #pygame.draw.rect(self.win, (0,255,0), (bullet.posX, bullet.posY,bullet.radius, bullet.radius) )       
            self.win.blit(pygame.transform.scale(bullet.image, (bullet.radius*2, bullet.radius*2)), (bullet.posX-bullet.radius, bullet.posY-bullet.radius))
            #pygame.draw.line(self.win, (0,0,255), (bullet.posX, bullet.posY),(bullet.posX+100, bullet.posY+100))

            if bullet.posY < 0:
                self.bulletsList.pop(indexBull)


    def updateBackgroundImage(self):
        gainSpeed = 0      
        if(self.userShip.currentDirection == 2):
            gainSpeed = self.userShip.speed/2
        if(self.userShip.currentDirection == -2):
            gainSpeed = -self.userShip.speed/5
        
        self.backgroundTimeTick += 1
        if self.backgroundTimeTick == 1:
            self.backgroundTimeTick = 0
            self.backgroundPosition += 0.5 + gainSpeed
            if self.backgroundPosition > self.winHeight:
                self.backgroundPosition = 0
        self.win.blit(self.imageBackgroundSpace, (0,self.backgroundPosition - self.winHeight))
        self.win.blit(self.imageBackgroundSpace, (0, self.backgroundPosition))



    def userShipUpdted(self):
        self.win.blit(self.userShip.image, (self.userShip.posX, self.userShip.posY))


    def updateDisplay(self):
        self.updateBackgroundImage()
        self.enemyAsteroidUpdated()
        self.userBulletsUpdted()
        self.userShipUpdted()       
        pygame.display.update()

    def main_process_update(self):
        self.eventTest()            
        self.keyTest()
        self.updateDisplay()


