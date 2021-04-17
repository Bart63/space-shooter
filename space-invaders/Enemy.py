import Invaders

class Enemy(Invaders):
    def __init__(self, x, y, health=100, movement_speed, collision_damage):
        self.x = x
        self.y = y
        self.health = health
        self.movement_speed = movement_speed
        self.collision_damage = collision_damage


    def move(self):
    def action(self):