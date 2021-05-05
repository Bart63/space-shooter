from Invaders.Invaders import Invaders
from GlobalVars import WIDTH

class Enemy(Invaders):
    def __init__(self, x, y, image, score=10, movement_speed=1, damage=1, 
                health=1, width=100, height=100, right=0, down=1, right_dir=True):
        super(Enemy, self).__init__(x, y, image, score, movement_speed, damage, 
                                    health, width, height, right, down)
        self.right_dir = right_dir

    def move(self):
        if self.x+self.width >= WIDTH and self.right_dir:
            self.right_dir = False
        elif self.x <= 0 and not self.right_dir:
            self.right_dir = True

        change_to_right = self.right_dir and self.right<0
        change_to_left = not self.right_dir and not self.right<0
        if change_to_right or change_to_left:
            self.right = -self.right

        super().move()