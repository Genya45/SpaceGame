#   класс вражеского астероида

import random


class EnemyAsteroid:
    def __init__(self, maxW, maxH, image, imageBoomList):
        #   размеры окна
        self.maxW = maxW
        self.maxH= maxH
        #   позиция
        self.posX = random.randint(1,maxW)
        self.posY = -10
        #   размеры (радиус)
        self.radius = random.randint(20,40)
        #   скорость полета по оси X и Y
        self.speedX = random.randint(1,6) - 3
        self.speedY = random.randint(4,7)

        #   изображение астероида
        self.image = image
        self.imageBoomList = imageBoomList
        self.imageNum = 0

        self.timeTick = 0
        self.timeTickMax = 10
        self.countLoopImageBoom = 0
        self.countLoopImageBoomMax = 5

        self.isBoom = False
        self.isDead = False

    def update_image_boom(self):
        self.timeTick += 1
        if self.timeTick == self.timeTickMax:
            self.timeTick = 0
            self.imageNum += 1
            self.countLoopImageBoom += 1
            if self.countLoopImageBoom ==  self.countLoopImageBoomMax:
                self.isDead = True

            if self.imageNum == len(self.imageBoomList):
                self.imageNum = 0
            self.image = self.imageBoomList[self.imageNum]

    #   обновление позиции
    def update_position(self):
        if self.isBoom:
            self.update_image_boom()
        else:
            self.posY += self.speedY
            self.posX += self.speedX

    #   проверка выхода за границы
    def isBorderOut(self):
        if self.posX > self.maxW or self.posX < 0 or self.posY > self.maxH:
            return True
        else:
            return False

        
if __name__ == "__main__":
    print("It is not a main module")