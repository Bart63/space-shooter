from Invaders import Shooter
import os
import random

class EnemyGenerator():
    ENEMY_IMG_1 = os.path.join('imgs', 'enemy_new_1.png')
    ENEMY_IMG_2 = os.path.join('imgs', 'enemy_new_2.png')
    ENEMY_LIST = []

    def __init__(self, width, time_range=1000, enemies=5):
        self.x_range=width
        self.populate_random(time_range, enemies)

    def populate_random(self, max_time=5000, how_many_enemies=10):
        times=[]
        time_left=max_time
        for _ in range(how_many_enemies):
            time = random.randrange(time_left)
            if time>time_left/2:
                time = int(time/2)
            times.append(time)
            time_left -= time
        
        for i in range(how_many_enemies):
            self.ENEMY_LIST.append({
                'obj' : Shooter(random.randrange(self.x_range), 0, self.ENEMY_IMG_1, width=56, height=40, right_dir=bool(random.getrandbits(1))),
                'time' : times[i]
            })