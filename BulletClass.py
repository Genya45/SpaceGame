import random


class Bullet:
    def __init__(self, posX, posY, speed = 10, image = None):
        self.posX = posX
        self.posY = posY
        self.radius = 10
        self.speed = speed
        self.image = image

    def update_position(self):
        self.posY -= self.speed
        #self.posX += random.randint(1,20) - 10