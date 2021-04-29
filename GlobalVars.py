from Powerups import FasterShip, HP, Shield
from os import path


fs = lambda ship: FasterShip(ship)
hp = lambda ship: HP(ship)
shi = lambda ship: Shield(ship)

powerups = [fs, hp, shi]
powers = [FasterShip, Shield, HP]

ENEMY_IMG_1_PATH = path.join('imgs', 'enemy_new_1.png')
ENEMY_IMG_2_PATH = path.join('imgs', 'enemy_new_2.png')
SHIP_IMG_PATH = path.join('imgs', 'gracz.png')
BULLET_IMG_PATH = path.join('imgs', 'bullet.png')
BG_IMG_PATH = path.join('imgs', 'background.png')
EXPLOSION_IMG_PATH = path.join('imgs', 'wybuch.png')
SHIELD_IMG_PATH = path.join('imgs', 'shield.png')
HP_IMG_PATH = path.join('imgs', 'HP.png')
RED = (255, 255, 0)
WHITE = (255, 255, 255)