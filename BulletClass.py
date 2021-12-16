class Bullet:
    def __init__(self, posX, posY):
        self.posX = posX
        self.posY = posY
        self.radius = 5
        self.speed = 7

    def update_position(self):
        self.posY -= self.speed