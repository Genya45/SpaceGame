#   класс пользовательского корабля, которым юзер и управляет

class UserShip:
    #   в конструкторе задаються основные параметры
    def __init__(self, posX, posY, maxW, maxH, imageList = None, height = 100, width = 100):
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
        self.health = 3

        #   изображение снаряда
        self.imageList = imageList
        self.imageNum = 0
        self.image = None
        self.timeTick = 9
        self.timeTickMax = 10
        self.flagCounter = 1

        self.currentDirection = 0

    
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

    def change_direction(self, direction):
        self._update_image()
        self.currentDirection = direction
        self.update_position()

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
