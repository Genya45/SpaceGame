#   класс пользовательского корабля, которым юзер и управляет

class UserShip:
    #   в конструкторе задаються основные параметры
    def __init__(self, posX, posY, maxW, maxH, imageList = None, imageBoomList = None, height = 100, width = 100):
        #   позиция
        self.posX = posX
        self.posY = posY
        #   размеры окна
        self.maxW = maxW
        self.maxH = maxH
        #   скорость
        self.speed = 5
        #   размеры
        self.height = height
        self.width = width
        #   текущее максимальное количество патронов (будет увеличиваться при развитии)
        self.maxCountBullets = 1
        #   скорость полета патронов
        self.bulletSpeed = 4
        #   текущее количество жизней 
        self.life = 3

        #   изображение снаряда
        self.imageList = imageList
        self.imageKeepList = imageList
        self.imageNum = 0
        self.image = None
        self.timeTick = 9
        self.timeTickMax = 10
        self.flagCounter = 1

        self.currentDirection = 0

        self.imageBoomList = imageBoomList
        self.isBoom = False
        self.timeTickBoom = 0
        self.timeTickMaxBoom = 200

    def shipBoom(self):
        self.life -= 1
        self.isBoom = True
        self.imageKeepList = self.imageList
    
    def _update_image(self):

        self.timeTick += 1
        if self.timeTick == self.timeTickMax:
            self.timeTick = 0

            self.imageNum += self.flagCounter
            if self.imageNum == len(self.imageList)-1:
                self.flagCounter = -1
            if self.imageNum == 0:                
                self.flagCounter = 1
            self.image = self.imageList[self.imageNum]

    def checkIsDead(self):        
        self.imageList = self.imageBoomList
        self.timeTickBoom += 1
        if self.timeTickBoom > self.timeTickMaxBoom:
            self.timeTickBoom = 0
            self.imageList = self.imageKeepList
            self.isBoom = False


    def change_direction(self, direction):
        if self.isBoom:
            self.checkIsDead()
        else:
            self.currentDirection = direction
            self.update_position()
        self._update_image()

    def update_position(self):

        if self.currentDirection == 1:
            if self.posX < self.maxW - self.width:
                self.posX += self.speed
        if self.currentDirection == -1:
            if self.posX > 0:
                self.posX -= self.speed
        if self.currentDirection == 2:
            #print(self.posY, self.maxW/2)
            if self.posY > self.maxH/2:
                self.posY -= self.speed
        if self.currentDirection == -2:
            if self.posY < self.maxH - self.height:
                self.posY += self.speed


if __name__ == "__main__":
    print("It is not a main module")