from Invaders.Enemy import Enemy

class Shooter(Enemy):
    def __init__(self, x, y, image, movement_speed=1, shooting_speed=1, collision_damage=1, health=100, 
                    width=48, height=69):
        super(Shooter, self).__init__(x, y, image, movement_speed, collision_damage, health, width, height)
        self.shooting_speed=shooting_speed