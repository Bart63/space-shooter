from Invaders.Invaders import Invaders

class Enemy(Invaders):
    def __init__(self, x, y, image, movement_speed=1, collision_damage=1, health=100, width=100, height=100, score=10):
        super(Enemy, self).__init__(x, y, image, movement_speed, collision_damage, health, width, height)
        self.score = score

    def move(self, down, right=0): # (popatrz na kolejnosc argumentow), A na przyszlosc poruszanie sie
        super().move(self.movement_speed*right, down*self.movement_speed)