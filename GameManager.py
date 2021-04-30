from Invaders import Ship
from Weapons import Bullet, Explosion
import pygame
from EnemyList import EnemyGenerator
from GlobalVars import *

pygame.font.init()
FONT = pygame.font.SysFont('comicsans', 40)
FONT_BIG = pygame.font.SysFont('comicsans', 100)
SHIP_PU = pygame.transform.scale(pygame.image.load(SHIP_IMG_PATH), (25, 25))
SHIELD_PU = pygame.transform.scale(pygame.image.load(SHIELD_IMG_PATH), (25, 25))
HP_PU = pygame.transform.scale(pygame.image.load(HP_IMG_PATH), (25, 25))
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space shooter")
BG_IMG = pygame.image.load(BG_IMG_PATH)
BG_IMG = pygame.transform.scale(BG_IMG, (WIDTH, HEIGHT))
EXPLOSION_IMG = pygame.image.load(EXPLOSION_IMG_PATH)
EXPLOSION_IMG = pygame.transform.scale(EXPLOSION_IMG, (69, 69))

class GameManager:
    def __init__(self):
        self.SHIP = Ship(WIDTH/2, HEIGHT-80, SHIP_IMG_PATH, 5)
        self.run = True
        self.ship_bullets = []
        self.enemy_bullets = []
        self.enemies = []
        self.explosions = []
        self.previous_ticks = 0
        self.EnemyGenerator = EnemyGenerator()

    def getDeltaTime(self):
        self.t = pygame.time.get_ticks()
        self.deltaTime = self.t-self.previous_ticks
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

    def quit_handle(self):
        if pygame.event.get(eventtype=pygame.QUIT):
            self.run = False

    def action(self):
        res = self.SHIP.action(self.deltaTime)
        if type(res)==Bullet:
            self.ship_bullets.append(res)
        elif type(res)==Explosion:
            self.explosions.append(res)
        for i, e in enumerate(self.enemies):
            res = e.action(self.deltaTime)
            if e.y > HEIGHT:
                e.die()
            if type(res)==Bullet:
                self.enemy_bullets.append(res)
            elif type(res)==Explosion:
                self.explosions.append(res)
            if not e.is_alive:
                del self.enemies[i]
        for i, e in enumerate(self.explosions):
            if e.damage < 0:
                del self.explosions[i]
            e.transform()
        res = self.SHIP.collision_handle(self.enemies)
        for i, r in enumerate(res):
            if r:
                self.enemies[i].die()

    def weapons_handle(self):
        for i, b in enumerate(self.ship_bullets):
            b.transform()
            if b.y < 0:
                del self.ship_bullets[i]
        for i, b in enumerate(self.enemy_bullets):
            b.transform()
            if b.y > HEIGHT:
                del self.enemy_bullets[i]
        for e in self.enemies:
            res = e.collision_handle(self.ship_bullets)
            for i, r in enumerate(res):
                if r:
                    self.SHIP.get_score(e.score)
                    e.die()
                    del self.ship_bullets[i]
                    self.SHIP.get_powerup()
        res = self.SHIP.collision_handle(self.enemy_bullets)
        for i, r in enumerate(res):
            if r:
                del self.enemy_bullets[i]
        res = self.SHIP.collision_handle(self.explosions)
        for i, r in enumerate(res):
            if r:
                del self.explosions[i]

    def draw(self):
        WIN.blit(BG_IMG, (0, 0))
        WIN.blit(self.SHIP.img, (self.SHIP.x, self.SHIP.y))
        for e in self.enemies:
            WIN.blit(e.img, (e.x, e.y))
        for b in self.enemy_bullets:
            WIN.blit(b.img, (b.x, b.y))
        for b in self.ship_bullets:
            WIN.blit(b.img, (b.x, b.y))
        for e in self.explosions:
            WIN.blit(e.img, (e.x, e.y))
        for p in self.SHIP.powerups:
            if powers.index(type(p))==0:
                WIN.blit(SHIP_PU, (5, HEIGHT-30))
            elif powers.index(type(p))==1:
                WIN.blit(SHIELD_PU, (35, HEIGHT-30))
            else:
                WIN.blit(HP_PU, (65, HEIGHT-30))
        health_text = FONT.render("Health: " + str(self.SHIP.health), 1, WHITE)
        score_text = FONT.render("Score: " + str(self.SHIP.score), 1, WHITE)
        WIN.blit(health_text, (WIDTH-health_text.get_width()-10, 10))
        WIN.blit(score_text, (10, 10))
        dead_text = "" if self.SHIP.is_alive else FONT_BIG.render("You are dead", 1, WHITE)
        if dead_text:
            WIN.blit(dead_text, (WIDTH/2-dead_text.get_width()/2, HEIGHT/2-dead_text.get_height()/2))
        pygame.display.update()

    def main(self):
        clock = pygame.time.Clock()
        while self.run:
            clock.tick(FPS)
            self.quit_handle()
            self.draw()
            if self.SHIP.is_alive:
                self.getDeltaTime()
                self.weapons_handle()
                self.action()
                self.spawnEnemies()
        pygame.quit()

if __name__ == "__main__":
    GameManager().main()