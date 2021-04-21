import pygame

class Weapon:
    def __init__(self, x, y, image, damage=1, width=5, height=5):
        self.x=x
        self.y=y
        self.img=pygame.transform.scale(pygame.image.load(image), (width, height))
        self.damage=damage
        self.width=width
        self.height=height

    def hit(self):
        pass