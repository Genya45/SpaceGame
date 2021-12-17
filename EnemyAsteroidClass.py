import random


class EnemyAsteroid:
    def __init__(self, maxW, maxH):
        self.maxW = maxW
        self.maxH= maxH
        self.posX = random.randint(1,maxW)
        self.posY = -10
        self.radius = random.randint(7,20)
        self.speedX = random.randint(1,6) - 3
        self.speedY = random.randint(4,7)

    def update_position(self):
        self.posY += self.speedY
        self.posX += self.speedX

    def isBorderOut(self):
        if self.posX > self.maxW or self.posX < 0 or self.posY > self.maxH:
            return True
        else:
            return False