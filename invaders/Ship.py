from Invaders.Invaders import Invaders

class Ship(Invaders):

    def __init__(self, x, y, image, movement_speed=1, shooting_speed=1, score=0, collision_damage=1, health=100, 
                    width=48, height=69):
        super(Ship, self).__init__(x, y, image, movement_speed, collision_damage, health, width, height)
        self.shooting_speed=shooting_speed
        self.score=score
    
    def getInput(self):
        pass

    def move(self, right, down):
        self.x+=right*self.movement_speed
        self.y+=down*self.movement_speed

    def shoot(self):
        pass

    def loose_healt(self):
        pass

    def die(self):
        pass