from Invaders.Enemy import Enemy
import random

class Shooter(Enemy):
    def __init__(self, x, y, image, movement_speed=1, shooting_speed=1, collision_damage=1, health=100, 
                    width=48, height=69, right_dir=True, shooting_dir=(1,0)):
        super(Shooter, self).__init__(x, y, image, movement_speed, collision_damage, health, width, height, right_dir)
        self.shooting_speed=shooting_speed
        self.shooting_dir=shooting_dir
        self.enemy_bullets=[]
        self.time_to_shoot = random.randint(10, 100)*10
        
    def shoot(self, bullet):
        self.enemy_bullets.append(bullet)

    def action(self, deltaTime):
        self.time_to_shoot-=deltaTime
        self.move_bullets()

    def move_bullets(self):
        for b in self.enemy_bullets:
            b.move(self.shooting_dir)