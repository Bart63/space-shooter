import Invaders

class Enemy(Invaders):
    def __init__(self, x, y, movement_speed, collision_damage, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.movement_speed = movement_speed
        self.collision_damage = collision_damage


    def move(self):
        pass

    def action(self):
        pass