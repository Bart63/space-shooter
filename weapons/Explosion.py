from Weapons.Weapon import Weapon
from GlobalVars import EXPLOSION_IMG_PATH
from pygame import transform, image as py_image

class Explosion(Weapon):
    def __init__(self, x, y, image=EXPLOSION_IMG_PATH, speed=1.01, damage=10, width=5, height=5):
        super(Explosion, self).__init__(x, y, image, speed, damage, width, height)

    def transform(self):
        delta_width = self.width*self.speed - self.width
        delta_height = self.height*self.speed - self.height
        self.width += delta_width
        self.height += delta_height
        self.x -= delta_width/2
        self.y -= delta_height/2
        self.damage -= 0.2
        super().transform()
        self.img = transform.scale(py_image.load(EXPLOSION_IMG_PATH), (int(self.width), int(self.height)))