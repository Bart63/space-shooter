from Weapons.Weapon import Weapon

class Bullet(Weapon):
    def __init__(self, x, y, image, speed=1, damage=1, width=5, height=5):
        super(Bullet, self).__init__(x, y, image, damage, width, height)
        self.speed=speed

    def move(self, down, right=0):
        self.x+=right*self.speed
        self.y+=down*self.speed
        
    def hit(self):
        pass