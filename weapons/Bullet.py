from Weapons.Weapon import Weapon
import pygame 

class Bullet(Weapon):
    def __init__(self, x, y, image, speed=1, damage=1, width=5, height=5):
        super(Bullet, self).__init__(x, y, image, damage, width, height)
        self.speed=speed
        self.Rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def move(self, direction):
        self.x+=direction[1]*self.speed
        self.y+=direction[0]*self.speed
        self.Rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
    def hit(self):
        pass