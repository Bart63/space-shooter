from Invaders import Invaders

class Ship(Invaders):

    def __init__(self, shooting_speed, score, x, y, movement_speed, collision_damage, image, health=100):
        super(Ship, self).__init__(x, y, movement_speed, collision_damage, image, health)
        self.shooting_speed=shooting_speed
        self.score=score
    
    def getInput(self):
        pass

    def move(self):
        pass

    def shoot(self):
        pass

    def loose_healt(self):
        pass

    def die(self):
        pass