from Invaders.Enemy import Enemy
from Weapons import Bullet
from random import randint
from GlobalVars import BULLET_IMG_PATH, ENEMY_IMG_1_PATH, ENEMY_HEIGHT, ENEMY_WIDTH

class Shooter(Enemy):
    def __init__(self, x, y, image=ENEMY_IMG_1_PATH, score=10, movement_speed=1, shooting_speed=1, damage=12, 
                health=1, width=ENEMY_WIDTH, height=ENEMY_HEIGHT, right=1, down=1, right_dir=True, shooting_dir=(1,0)):
        super(Shooter, self).__init__(x, y, image, score, movement_speed, damage, health, width, height, right, down, right_dir)
        self.shooting_speed = shooting_speed
        self.shooting_dir = shooting_dir
        self.time_to_shoot = self.calc_rand_time()
        
    def shoot(self):
        bullet = Bullet(int(self.x + self.width/2), self.y+10, direction=self.shooting_dir, speed=6)
        return bullet

    def calc_rand_time(self):
        return randint(10, 100)*10

    def action(self, deltaTime):
        super().action()
        if self.is_alive:
            self.time_to_shoot -= deltaTime
            if self.time_to_shoot <= 0:
                self.time_to_shoot = self.calc_rand_time()
                return self.shoot()
        