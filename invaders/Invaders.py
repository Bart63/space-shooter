import pygame

class Invaders:
    def __init__(self, x, y,  image, movement_speed=1, collision_damage=1, health=100, width=100, height=100):
        self.x=x
        self.y=y
        self.health=health
        self.movement_speed=movement_speed
        self.collision_damage=collision_damage
        self.img=pygame.transform.scale(pygame.image.load(image), (width, height))
        self.width=width
        self.height=height
        self.Rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def move(self, right, down):
        self.x+=right*self.movement_speed
        self.y+=down*self.movement_speed
        self.Rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def loose_healt(self, damage):
        self.health -= damage