from Invaders import Shooter

ENEMY_IMG_1 = os.path.join('imgs', 'enemy_new_1.png')
ENEMY_IMG_2 = os.path.join('imgs', 'enemy_new_2.png')

ENEMY_LIST = [
    {
        obj : Shooter(10, 0, ENEMY_IMG_1),
        time : 500
    },
    {
        obj : Shooter(30, 0, ENEMY_IMG_1),
        time : 5
    },
]