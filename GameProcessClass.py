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

        self.__FONT_SCORE_PATH__ = 'assets/fonts/Space Age.ttf'
        self.fontScore = None
        self.__FONT_GAME_OVER_PATH__ = 'assets/fonts/blocked.ttf'
        self.fontGameOver = None
        self.__FONT_CONTINUE_PATH__ = 'assets/fonts/solid.ttf'
        self.fontContinue = None

        self.__IMG_PATH_ASTEROIDS__ = "assets/images/asteroids/"
        self.__IMG_PATH_ASTEROIDS_BOOM__ = "assets/images/asteroidsBoom/"
        self.__IMG_PATH_BKG_SPACE__ = "assets/images/backgrounds/"
        self.__IMG_PATH_STAR_SHIP__ = "assets/images/userStarShips/"
        self.__IMG_PATH_USER_BULLET__ = "assets/images/userBullets/"

        self.bulletsList = []

        self.enemyAsteroidTicksMax = 100
        self.enemyAsteroidTicks = 0
        self.enemyAsteroidList = []
        self.asteroidsListImages = []
        
        self.backgroundTimeTick = 0
        self.backgroundTimeTickMax = 10
        self.backgroundPosition = 0


        self.scoreTickTime = 0
        self.scoreTickTimeMax = 10
        self.score = 0

        self.songShot = None
        self.__SONG_SHOT_PATH__ = 'assets/sounds/Shot.mp3'
        self.songBoomAsteroid = None
        self.__SONG_BOOM_ATEROID_PATH__ = 'assets/sounds/Crash.mp3'
        self.songBoomUserShip = None
        self.__SONG_BOOM_USER_SHIP_PATH__ = 'assets/sounds/Crash.mp3'
        self.songGameOver = None
        self.__S0NG_GAME_OVER_PATH__ = 'assets/sounds/GameOver.mp3'
        
        self.__MUSIC_BACKGROUND_PATH__ = 'assets/music/GameProcess/'

        self.userShip = UserShip(self.winWidth/2, self.winHeight-self.winHeight/3, self.winWidth, self.winHeight)

        self.isGameOver = False

        self.imageLoader()
        self.fontLoader()
        self.songLoader()


    def imageLoader(self):
        for imageAsteroid in os.listdir(self.__IMG_PATH_ASTEROIDS__):       
            asteroidImage = pygame.image.load(self.__IMG_PATH_ASTEROIDS__ + imageAsteroid)
            #asteroidImage = pygame.transform.scale(asteroidImage, (50,50))
            self.asteroidsListImages.append(asteroidImage)
        
        for imageAteroidBoom in os.listdir(self.__IMG_PATH_ASTEROIDS_BOOM__):
            imageBoom = pygame.image.load(self.__IMG_PATH_ASTEROIDS_BOOM__ + imageAteroidBoom)
            self.enemyAsteroidBoomImagesList.append(imageBoom)
        
        for imageStarship in os.listdir(self.__IMG_PATH_STAR_SHIP__):
            imgStarship = pygame.image.load(self.__IMG_PATH_STAR_SHIP__ + imageStarship)
            imgStarship = pygame.transform.scale(imgStarship, (self.userShip.width, self.userShip.height))
            self.imageStarShipList.append(imgStarship)
        self.userShip.imageList = self.imageStarShipList
        self.userShip.imageBoomList = self.enemyAsteroidBoomImagesList
        for i in range(0, len(self.enemyAsteroidBoomImagesList)):
                self.userShip.imageBoomList[i] = pygame.transform.scale(self.userShip.imageBoomList[i], (self.userShip.width, self.userShip.height))


        for imageBullet in os.listdir(self.__IMG_PATH_USER_BULLET__):
            image = pygame.image.load(self.__IMG_PATH_USER_BULLET__ + imageBullet)
            #image = pygame.transform.scale(image, (20,20))
            self.userBulletImagesList.append(image)

    def fontLoader(self):
        self.fontScore = pygame.font.Font(self.__FONT_SCORE_PATH__, 30)
        self.fontContinue = pygame.font.Font(self.__FONT_CONTINUE_PATH__, 30)
        self.fontGameOver = pygame.font.Font(self.__FONT_GAME_OVER_PATH__, 70)
    
    def songLoader(self):        
        self.songShot = pygame.mixer.Sound(self.__SONG_SHOT_PATH__)
        self.songGameOver = pygame.mixer.Sound(self.__S0NG_GAME_OVER_PATH__)
        self.songBoomAsteroid = pygame.mixer.Sound(self.__SONG_BOOM_ATEROID_PATH__)
        self.songBoomUserShip = pygame.mixer.Sound(self.__SONG_BOOM_USER_SHIP_PATH__)
        
        
        listMusic = os.listdir(self.__MUSIC_BACKGROUND_PATH__)
        musicNum = random.randint(0, len(listMusic) - 1)
        
        pygame.mixer.music.load(self.__MUSIC_BACKGROUND_PATH__ + listMusic[musicNum])
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play()







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
                        self.songBoomAsteroid.play()
                        self.score += 100
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
                        (enemyAsteroid.posY < (self.userShip.posY + self.userShip.height + enemyAsteroid.radius) and
                        self.userShip.isBoom == False):
                    self.userShip.shipBoom()
                    self.songBoomUserShip.play()
                    if self.userShip.life <= 0:
                        self.isGameOver = True
                        self.songGameOver.play()
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
                self.imageBackgroundSpace = pygame.image.load(self.__IMG_PATH_BKG_SPACE__ + os.listdir(self.__IMG_PATH_BKG_SPACE__)[self.imageBackgroundSpaceNumber])               
                self.imageBackgroundSpace = pygame.transform.scale(self.imageBackgroundSpace, self.win.get_size())

            if event.type == pygame.QUIT:
                self.isRunMainLoop = False
                pygame.mixer.music.stop()
                break
            if event.type == pygame.KEYDOWN:                        
                if event.key == pygame.K_ESCAPE:
                    self.isRunMainLoop = False
                    pygame.mixer.music.stop()
                    break
                if event.key == pygame.K_RETURN and self.isGameOver:
                    self.isRunMainLoop = False
                    pygame.mixer.music.stop()
                    break
                if event.key == pygame.K_SPACE:
                    if len(self.bulletsList) < self.userShip.maxCountBullets and self.userShip.isBoom == False:
                        self.bulletsList.append(Bullet(self.userShip.posX + self.userShip.width / 2, self.userShip.posY-5, self.userBulletImagesList.copy(), self.userShip.bulletSpeed))
                        self.songShot.play()

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

    def updateScore(self):
        if(self.userShip.currentDirection == 2):
            self.scoreTickTimeMax = 5
        elif(self.userShip.currentDirection == -2):
            self.scoreTickTimeMax = 20
        else:
            self.scoreTickTimeMax = 10

        self.scoreTickTime += 1
        if self.scoreTickTime >= self.scoreTickTimeMax:
            self.scoreTickTime = 0
            self.score += 1

    def printDisplayText(self):  
        text = 'Score: ' + str(self.score)
        fontScoreDisplay = self.fontScore.render(text , False, (0, 255, 0))
        position = [10, self.win.get_size()[1] - (self.fontScore.size(text)[1])] 
        self.win.blit(fontScoreDisplay, position)
    
    def printDisplayUserLife(self):         
        text = 'X ' + str(self.userShip.life)
        fontDisplay = self.fontContinue.render(text , False, (0, 255, 0))
        position = [self.win.get_size()[0] - self.fontContinue.size(text)[0], self.win.get_size()[1] - self.fontContinue.size(text)[1]]
        position[0] -= 10
        position[1] -= 10
        self.win.blit(fontDisplay, position) 

        image = self.imageStarShipList[0]
        image = pygame.transform.scale(image, (50,50))
        position[0] = position[0] - (image.get_size()[0] + 10)
        position[1] -= 10
        self.win.blit(image, position) 
        



    def userShipUpdted(self):
        self.win.blit(self.userShip.image, (self.userShip.posX, self.userShip.posY))

    def gameOver(self):
        listWinSize = list(self.win.get_size())
        rectBcg = listWinSize.copy()
        rectBcg[0] /= 4
        rectBcg[1] /= 4
        rectBcg.append(listWinSize.copy()[0]/2)
        rectBcg.append(listWinSize.copy()[1]/2)
        pygame.draw.rect(self.win, (0, 0, 0), (rectBcg))   
        
        

        text = 'GAME OVER'
        fontDisplay = self.fontGameOver.render(text , False, (255, 0, 0))
        position = []
        position.append(self.win.get_size()[0]/2 - self.fontGameOver.size(text)[0]/2)
        position.append(self.win.get_size()[1]/4 + self.fontGameOver.size(text)[1]/2)
        self.win.blit(fontDisplay, position) 
        
        
        text = 'Score:'
        fontDisplay = self.fontScore.render(text , False, (0, 255, 0))
        position = []
        position.append(self.win.get_size()[0]/3 - self.fontScore.size(text)[0]/2)
        position.append(self.win.get_size()[1]/2)
        self.win.blit(fontDisplay, position) 

        text = str(self.score)
        fontDisplay = self.fontScore.render(text , False, (0, 255, 0))
        position = []
        position.append(self.win.get_size()[0] - self.win.get_size()[0]/3 - self.fontScore.size(text)[0]/2)
        position.append(self.win.get_size()[1]/2)
        self.win.blit(fontDisplay, position)    

        
        text = 'PRESS ENTER TO CONTINUE'
        fontDisplay = self.fontContinue.render(text , False, (255, 0, 0))
        position = []
        position.append(self.win.get_size()[0]/2 - self.fontContinue.size(text)[0]/2)
        position.append((self.win.get_size()[1]/4 + self.win.get_size()[1]/2) - self.fontContinue.size(text)[1]*2)
        self.win.blit(fontDisplay, position) 



    def updateDisplay(self):
        self.updateBackgroundImage()
        if self.isGameOver:
            self.gameOver()   
        else:            
            self.updateScore()
            self.printDisplayText()
            self.printDisplayUserLife()
            self.userBulletsUpdted()
            self.userShipUpdted()   
        self.enemyAsteroidUpdated()
        pygame.display.update()

    def main_process_update(self):
        self.eventTest()            
        self.keyTest()
        self.updateDisplay()


if __name__ == "__main__":
    print("It is not a main module")