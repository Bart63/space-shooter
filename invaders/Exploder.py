from Invaders.Enemy import Enemy
from Weapons.Explosion import Explosion
from GlobalVars import EXPLOSION_IMG_PATH, ENEMY_IMG_2_PATH, ENEMY_HEIGHT, ENEMY_WIDTH

class Exploder(Enemy):
    def __init__(self, x, y, image=ENEMY_IMG_2_PATH, score=20, movement_speed=1, damage=15, health=1, 
                    width=ENEMY_WIDTH, height=ENEMY_HEIGHT, right=0, down=1, right_dir=True):
        super(Exploder, self).__init__(x, y, image, score, movement_speed, damage, health, width, height, 
                                        right, down, right_dir)

    def action(self, deltaTime):
        if not self.is_alive:
            return self.explode()
        super().action()
        self.movement_speed += deltaTime/500

    def explode(self):
        return Explosion(self.x, self.y, width=self.width, height=self.height)