import Invaders

class Enemy(Invaders):
    def __init__(self, x, y, image, movement_speed=1, collision_damage=1, health=100):
        super(Enemy, self).__init__(x, y, image, movement_speed, collision_damage, health)

    def move(self):
        pass

    def action(self):
        pass