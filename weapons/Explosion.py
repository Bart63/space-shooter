from Weapons.Weapon import Weapon
import pygame 

class Explosion(Weapon):
    def __init__(self, x, y, image, speed=1, damage=10, width=5, height=5):
        super(Explosion, self).__init__(x, y, image, speed, damage, width, height)

    def transform(self):
        self.width = self.width*self.speed
        self.height = self.height*self.speed
        super().transform()