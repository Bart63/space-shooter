from Weapons.Weapon import Weapon
import pygame 

class Bullet(Weapon):
    def __init__(self, x, y, image, direction=(0,1), speed=1, damage=1, width=5, height=5):
        super(Bullet, self).__init__(x, y, image, damage, width, height)
        self.speed = speed
        self.Rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.direction = direction

    def move(self):
        self.x+=self.direction[1]*self.speed
        self.y+=self.direction[0]*self.speed
        self.Rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
    def hit(self):
        pass