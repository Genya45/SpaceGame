class UserShip:
    def __init__(self, posX, posY, height = 50, width = 50):
        self.posX = posX
        self.posY = posY
        self.speed = 5
        self.height = height
        self.width = width
        self.maxCountBullets = 1
        self.bulletSpeed = 4

    #def update_position(self):
    #    self.posY -= self.speed