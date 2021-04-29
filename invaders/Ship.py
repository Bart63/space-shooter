from Invaders.Invaders import Invaders
from Weapons import Bullet

class Ship(Invaders):

    def __init__(self, x, y, image, movement_speed=1, shooting_speed=1, score=0, collision_damage=1, health=100, 
                    width=48, height=69, shooting_dir=(-1,0)):
        super(Ship, self).__init__(x, y, image, movement_speed, collision_damage, health, width, height)
        self.shooting_speed = shooting_speed
        self.score = score
        self.shooting_dir = shooting_dir
        self.powerups = []

    def shoot(self, bullet_img):
        bullet = Bullet(int(self.x + self.width/2), self.y-10, bullet_img, direction=(-1, 0), speed=6)
        return bullet
        
    def action(self, deltaTime):
        for i, p in enumerate(self.powerups):
            p.check_time(deltaTime)
            if p.is_active:
                p.action()
            else:
                del self.powerups[i]
            
    def get_score(self, points):
        self.score += points

    def die(self):
        pass