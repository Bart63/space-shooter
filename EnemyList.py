from Invaders import Shooter, Exploder
from GlobalVars import ENEMY_IMG_1_PATH, ENEMY_IMG_2_PATH
import random

class EnemyGenerator():
    ENEMY_LIST = []
    prob_fact = 10
    iter=0

    def __init__(self, width, time_range=1000, enemies=5):
        self.x_range=width
        self.populate_random(time_range, enemies)

    def populate_random(self, max_time=5000, how_many_enemies=5):
        times=[]
        time_left=max_time
        how_many_enemies += self.iter
        for _ in range(how_many_enemies):
            time = random.randrange(time_left)
            if time>time_left/2:
                time = int(time/2)
            times.append(time)
            time_left -= time
        
        for i in range(how_many_enemies):
            if(random.random()>(self.iter/(self.iter+self.prob_fact))):
                self.ENEMY_LIST.append({
                    'obj' : Shooter(random.randrange(self.x_range), 0, ENEMY_IMG_1_PATH, width=56, height=40, right_dir=bool(random.getrandbits(1))),
                    'time' : times[i]
                })
            else:
                self.ENEMY_LIST.append({
                    'obj' : Exploder(random.randrange(self.x_range), 0, ENEMY_IMG_2_PATH, width=56, height=40),
                    'time' : times[i]
                })
        self.iter+=1