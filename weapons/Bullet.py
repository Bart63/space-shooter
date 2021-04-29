from Weapons.Weapon import Weapon
import pygame 

class Bullet(Weapon):
    def __init__(self, x, y, image, direction=(0,1), speed=1, damage=10, width=5, height=5):
        super(Bullet, self).__init__(x, y, image, speed, damage, width, height)
        self.direction = direction

    def transform(self):
        self.x+=self.direction[1]*self.speed
        self.y+=self.direction[0]*self.speed
        super().transform()