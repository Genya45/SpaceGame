import random


class Bullet:
    def __init__(self, posX, posY, speed = 10):
        self.posX = posX
        self.posY = posY
        self.radius = 5
        self.speed = speed

    def update_position(self):
        self.posY -= self.speed
        #self.posX += random.randint(1,20) - 10