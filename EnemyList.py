from Invaders import Shooter
import os
import random

ENEMY_IMG_1 = os.path.join('imgs', 'enemy_new_1.png')
ENEMY_IMG_2 = os.path.join('imgs', 'enemy_new_2.png')

ENEMY_LIST = [
    {
        'obj' : Shooter(100, 0, ENEMY_IMG_1, width=56, height=40, right_dir=False),
        'time' : 500
    }
]

def populate_random(max_time, how_many_enemies):
    times=[]
    time_left=max_time
    for _ in range(how_many_enemies):
        time = random.randint(0, time_left)
        if time>(max_time/2):
            time=int(time/2)
        times.append(time)
        time_left -= time
    
    for i in range(how_many_enemies):
        ENEMY_LIST.append({
            'obj' : Shooter(random.randint(1,800), 0, ENEMY_IMG_1, width=56, height=40, right_dir=bool(random.getrandbits(1))),
            'time' : times[i]
        })

populate_random(1000, 10)