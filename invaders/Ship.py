from Invaders.Invaders import Invaders

class Ship(Invaders):

    def __init__(self, x, y, image, movement_speed=1, shooting_speed=1, score=0, collision_damage=1, health=100, 
                    width=48, height=69, shooting_dir=(-1,0)):
        super(Ship, self).__init__(x, y, image, movement_speed, collision_damage, health, width, height)
        self.shooting_speed=shooting_speed
        self.score=score
        self.shooting_dir=shooting_dir
        self.ship_bullets = []

    def shoot(self, bullet):
        self.ship_bullets.append(bullet)

    def action(self):
        self.move_bullets()

    def move_bullets(self):
        for b in self.ship_bullets:
            b.move(self.shooting_dir)

    def loose_healt(self):
        pass

    def die(self):
        pass