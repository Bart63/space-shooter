from Invaders import Ship
from Weapons import Bullet
import pygame
from EnemyList import EnemyGenerator
from GlobalVars import *
from random import randint, random

pygame.font.init()
FONT = pygame.font.SysFont('comicsans', 40)
FONT_BIG = pygame.font.SysFont('comicsans', 100)
SHIP_PU=pygame.transform.scale(pygame.image.load(SHIP_IMG_PATH), (25, 25))
SHIELD_PU=pygame.transform.scale(pygame.image.load(SHIELD_IMG_PATH), (25, 25))
HP_PU=pygame.transform.scale(pygame.image.load(HP_IMG_PATH), (25, 25))

class GameManager:
    WIDTH, HEIGHT = 700, 700
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Space shooter")
    FPS = 60
    BG_IMG = pygame.image.load(BG_IMG_PATH)
    BG_IMG = pygame.transform.scale(BG_IMG, (WIDTH, HEIGHT))
    EXPLOSION_IMG = pygame.image.load(EXPLOSION_IMG_PATH)
    EXPLOSION_IMG = pygame.transform.scale(EXPLOSION_IMG, (69, 69))

    def __init__(self):
        self.SHIP = Ship(self.WIDTH/2, self.HEIGHT-80, SHIP_IMG_PATH, 5)
        self.alive = True
        self.run = True
        self.ship_bullets = []
        self.enemy_bullets = []
        self.enemies = []
        self.previous_ticks = 0
        self.EnemyGenerator = EnemyGenerator(self.WIDTH)

    def getDeltaTime(self):
        self.t = pygame.time.get_ticks()
        self.deltaTime = (self.t-self.previous_ticks)
        self.previous_ticks = self.t

    def spawnEnemies(self):
        ENEMY_LIST = self.EnemyGenerator.ENEMY_LIST
        if len(ENEMY_LIST)==0:
            if len(self.enemies)==0:
                self.EnemyGenerator.populate_next_wave()
            return
        time_to_spawn = ENEMY_LIST[0]['time']-self.deltaTime
        if(time_to_spawn<=0):
            self.enemies.append(ENEMY_LIST[0]['obj'])
            del ENEMY_LIST[0]
        else:
            ENEMY_LIST[0]['time'] = time_to_spawn

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            if event.type == pygame.KEYDOWN and self.alive:
                if event.key == pygame.K_SPACE:
                    self.ship_bullets.append(self.SHIP.shoot(BULLET_IMG_PATH))

    def action(self):
        self.SHIP.action(self.deltaTime)
        for i, b in enumerate(self.ship_bullets):
            b.move()
            if b.y<0:
                del self.ship_bullets[i]
        for i, b in enumerate(self.enemy_bullets):
            b.move()
            if b.y>self.HEIGHT:
                del self.enemy_bullets[i]
        for i, e in enumerate(self.enemies):
            if hasattr(e, 'action'):
                e.action(self.deltaTime)
                if(e.time_to_shoot<=0):
                    self.enemy_bullets.append(e.shoot(BULLET_IMG_PATH))
                    e.time_to_shoot=randint(10, 100)*10
                e.move((self.WIDTH, self.HEIGHT))
            else:
                e.move()
            if e.y>self.HEIGHT:
                del self.enemies[i]

    def shooting_handle(self):
        for i, b in enumerate(self.ship_bullets):
            for j, e in enumerate(self.enemies):
                if b.Rect.colliderect(e.Rect):
                    self.SHIP.get_score(e.score)
                    del self.ship_bullets[i]
                    del self.enemies[j]
                    if random()>0.9:
                        powerup = powerups[randint(0, len(powerups)-1)](self.SHIP)
                        types = [type(p) for p in self.SHIP.powerups]
                        if type(powerup) in types:
                            k = types.index(type(powerup))
                            self.SHIP.powerups[k].desactivation()
                        self.SHIP.powerups.append(powerup)
        for i, b in enumerate(self.enemy_bullets):
            if b.Rect.colliderect(self.SHIP.Rect):
                self.SHIP.loose_healt(b.damage)
                del self.enemy_bullets[i]

    def ship_collision(self):
        for i, e in enumerate(self.enemies):
            if self.SHIP.Rect.colliderect(e.Rect):
                self.SHIP.loose_healt(e.collision_damage)
                del self.enemies[i]

    def is_ship_alive(self):
        if self.SHIP.health <= 0:
            self.alive = False
            self.SHIP.img=self.EXPLOSION_IMG

    def draw(self):
        self.WIN.blit(self.BG_IMG, (0, 0))

        health_text = FONT.render("Health: " + str(self.SHIP.health), 1, WHITE)
        score_text = FONT.render("Score: " + str(self.SHIP.score), 1, WHITE)
        dead_text = "" if self.alive else FONT_BIG.render("You are dead", 1, WHITE)
        self.WIN.blit(health_text, (self.WIDTH-health_text.get_width()-10, 10))
        self.WIN.blit(score_text, (10, 10))
        if dead_text:
            self.WIN.blit(dead_text, (self.WIDTH/2-dead_text.get_width()/2, self.HEIGHT/2-dead_text.get_height()/2))

        self.WIN.blit(self.SHIP.img, (self.SHIP.x, self.SHIP.y))

        for enemy in self.enemies:
            self.WIN.blit(enemy.img, (enemy.x, enemy.y))
        for bullet in self.enemy_bullets:
            self.WIN.blit(bullet.img, (bullet.x, bullet.y))
        for bullet in self.ship_bullets:
            self.WIN.blit(bullet.img, (bullet.x, bullet.y))

        for p in self.SHIP.powerups:
            if powers.index(type(p))==0:
                self.WIN.blit(SHIP_PU, (5, self.HEIGHT-30))
            elif powers.index(type(p))==1:
                self.WIN.blit(SHIELD_PU, (35, self.HEIGHT-30))
            else:
                self.WIN.blit(HP_PU, (65, self.HEIGHT-30))
        pygame.display.update()

    def key_manager(self):
        keys_pressed = pygame.key.get_pressed()

        right, down = 0, 0
        if (keys_pressed[pygame.K_d] or keys_pressed[pygame.K_RIGHT]) and self.SHIP.x<self.WIDTH-self.SHIP.width:
            right+=1
        if (keys_pressed[pygame.K_a] or keys_pressed[pygame.K_LEFT]) and self.SHIP.x>0:
            right-=1
        if (keys_pressed[pygame.K_s] or keys_pressed[pygame.K_DOWN]) and self.SHIP.y<self.HEIGHT-self.SHIP.height:
            down+=1
        if (keys_pressed[pygame.K_w] or keys_pressed[pygame.K_UP]) and self.SHIP.y>0:
            down-=1
        self.SHIP.move(right, down)

    def main(self):
        clock = pygame.time.Clock()
        while self.run:
            clock.tick(self.FPS)
            self.getDeltaTime()
            self.check_events()
            self.action()
            self.draw()
            if self.alive:
                self.spawnEnemies()
                self.key_manager()
                self.shooting_handle()
                self.ship_collision()
                self.is_ship_alive()
        pygame.quit()

if __name__ == "__main__":
    GameManager().main()