from Invaders.Enemy import Enemy

movement_speed = 2

class Exploder(Enemy):
    def __init__(self, x, y, image, movement_speed=1, collision_damage=1, health=100, 
                    width=48, height=69):
        super(Exploder, self).__init__(x, y, image, movement_speed, collision_damage, health, width, height)

    def move(self, down=movement_speed):
        super().move(down*self.movement_speed)