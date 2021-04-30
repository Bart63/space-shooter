from pygame import image as py_image, transform, Rect

class Weapon:
    def __init__(self, x, y, image, speed=1, damage=1, width=5, height=5):
        self.x = x
        self.y = y
        self.img = transform.scale(py_image.load(image), (width, height))
        self.speed = speed
        self.damage = damage
        self.width = width
        self.height = height
        self.Rect = Rect(x, y, width, height)

    def transform(self):
        self.Rect = Rect(self.x, self.y, self.width, self.height)