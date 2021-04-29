import pygame

class Weapon:
    def __init__(self, x, y, image, speed=1, damage=1, width=5, height=5):
        self.x=x
        self.y=y
        self.img=pygame.transform.scale(pygame.image.load(image), (width, height))
        self.speed=speed
        self.damage=damage
        self.width=width
        self.height=height
        self.Rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def transform(self):
        self.Rect = pygame.Rect(self.x, self.y, self.width, self.height)