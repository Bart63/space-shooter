from Invaders.Invaders import Invaders

class Enemy(Invaders):
    def __init__(self, x, y, image, movement_speed=1, collision_damage=1, health=100, width=100, height=100):
        super(Enemy, self).__init__(x, y, image, movement_speed, collision_damage, health, width, height)
        self.right_dir=True

    def move(self, boundaries):
        if self.x+self.width>=boundaries[0]:
            self.right_dir=False
        elif self.x<=0:
            self.right_dir=True
        
        right=-1
        if(self.right_dir):
            right=1
        
        super().move(self.movement_speed*right, self.movement_speed)

    def action(self):
        pass