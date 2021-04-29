from Invaders.Enemy import Enemy
from GlobalVars import EXPLOSION_IMG_PATH
import pygame

movement_speed = 2

class Exploder(Enemy):
    def __init__(self, x, y, image, movement_speed=1, collision_damage=20, health=100, 
                    width=48, height=69):
        super(Exploder, self).__init__(x, y, image, movement_speed, collision_damage, health, width, height)

    def move(self, down=movement_speed):
        super().move(down*self.movement_speed)

    def explode(self):
        self.img=pygame.transform.scale(pygame.image.load(EXPLOSION_IMG_PATH), (self.width+5, self.height+10))
        self.health -= 2
        self.movement_speed = 0.3