#   класс снарядов, выпущенных клавным кораблем

class Bullet:
    def __init__(self, posX, posY, imageList, speed = 10):
        #   позиция
        self.posX = posX
        self.posY = posY
        #   размер (радиус)
        self.radius = 10
        #   скорость
        self.speed = speed
        #   изображение снаряда
        self.imageList = imageList
        self.imageNum = 0
        self.image = imageList[self.imageNum]
        self.timeTick = 0
        self.timeTickMax = 10

    def _update_image(self):
        self.timeTick += 1
        if self.timeTick == self.timeTickMax:
            self.timeTick = 0
            self.imageNum += 1
            if self.imageNum == len(self.imageList):
                self.imageNum = 0
            self.image = self.imageList[self.imageNum]



    #   метод обновления позиции
    def update_position(self):
        self.posY -= self.speed
        self._update_image()
        
        #self.posX += random.randint(1,20) - 10