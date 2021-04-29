from Invaders import Shooter, Exploder
from GlobalVars import ENEMY_IMG_1_PATH, ENEMY_IMG_2_PATH
from random import random, randrange, getrandbits

class EnemyGenerator():
    ENEMY_LIST = []
    prob_fact = 10
    iter=0

    def __init__(self, width, time_range=1000, enemies=5):
        self.x_range = width
        self.populate_next_wave(time_range, enemies)

    def populate_next_wave(self, max_time=5000, how_many_enemies=5):
        times=[]
        time_left=max_time
        how_many_enemies += self.iter
        for _ in range(how_many_enemies):
            time = randrange(time_left)
            if time>time_left/2:
                time = int(time/2)
            times.append(time)
            time_left -= time
        
        for i in range(how_many_enemies):
            enemy_chances = self.iter/(self.iter+self.prob_fact)
            if(random()>enemy_chances): # x/(x+a)
                self.ENEMY_LIST.append({
                    'obj' : Shooter(randrange(self.x_range), 0, ENEMY_IMG_1_PATH, width=56, height=40, right_dir=bool(getrandbits(1))),
                    'time' : times[i]
                })
            else:
                self.ENEMY_LIST.append({
                    'obj' : Exploder(randrange(self.x_range), 0, ENEMY_IMG_2_PATH, width=56, height=40),
                    'time' : times[i]
                })
        self.iter+=1