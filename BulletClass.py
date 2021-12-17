import random


class Bullet:
    def __init__(self, posX, posY):
        self.posX = posX
        self.posY = posY
        self.radius = 5
        self.speed = 10

    def update_position(self):
        self.posY -= self.speed
        #self.posX += random.randint(1,20) - 10