from Invaders import Shooter
import os

ENEMY_IMG_1 = os.path.join('imgs', 'enemy_new_1.png')
ENEMY_IMG_2 = os.path.join('imgs', 'enemy_new_2.png')

ENEMY_LIST = [
    {
        'obj' : Shooter(100, 100, ENEMY_IMG_1, width=56, height=40),
        'time' : 500
    },
    {
        'obj' : Shooter(300, 100, ENEMY_IMG_1, width=56, height=40),
        'time' : 5
    }
]