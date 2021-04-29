from Invaders.Enemy import Enemy
from Weapons import Bullet
from random import randint

class Shooter(Enemy):
    def __init__(self, x, y, image, movement_speed=1, shooting_speed=1, collision_damage=1, health=100, 
                    width=48, height=69, right_dir=True, shooting_dir=(1,0)):
        super(Shooter, self).__init__(x, y, image, movement_speed, collision_damage, health, width, height)
        self.shooting_speed = shooting_speed
        self.shooting_dir = shooting_dir
        self.right_dir = right_dir
        self.time_to_shoot = randint(10, 100)*10
        
    def shoot(self, bullet_img):
        bullet = Bullet(int(self.x + self.width/2), self.y+10, bullet_img, direction=(1, 0), speed=6)
        return bullet

    def action(self, deltaTime):
        self.time_to_shoot -= deltaTime

    def move(self, boundaries, down=1, right=1): # Do Directions która rozumie granice planszy, rozumie poruszanie sie
        if self.x+self.width >= boundaries[0]:
            self.right_dir = False
        elif self.x <= 0:
            self.right_dir = True
        
        if(not self.right_dir):
            right =- right
        super().move(self.movement_speed*down, self.movement_speed*right)