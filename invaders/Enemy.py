import Invaders

class Enemy(Invaders):
    def __init__(self, x, y, movement_speed, collision_damage, image, health=100):
        super(Enemy, self).__init__(x, y, movement_speed, collision_damage, image, health)

    def move(self):
        pass

    def action(self):
        pass