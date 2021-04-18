import pygame

class Invaders:
    def __init__(self, x, y, movement_speed, collision_damage, image, health=100):
        self.x=x
        self.y=y
        self.health=health
        self.movement_speed=movement_speed
        self.collision_damage=collision_damage
        self.img=pygame.image.load(image)

    def move(self):
        pass

    def loose_healt(self):
        pass

    def colide(self):
        pass

    def die(self):
        pass