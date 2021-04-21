import os
from Invaders import Ship
from Weapons import Bullet
import pygame
from EnemyList import ENEMY_LIST

RED = (255, 255, 0)

class GameManager:
    WIDTH, HEIGHT = 700, 700
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Space shooter")
    FPS = 60
    BG_IMG = pygame.image.load(os.path.join('imgs', 'background.png'))
    BG_IMG = pygame.transform.scale(BG_IMG, (WIDTH, HEIGHT))
    SHIP_IMG_PATH = os.path.join('imgs', 'gracz.png')
    BULLET_IMG = os.path.join('imgs', 'bullet.png')

    def __init__(self):
        self.SHIP = Ship(self.WIDTH/2, self.HEIGHT-80, self.SHIP_IMG_PATH, 5)
        self.run = True
        self.ship_bullets = []
        self.enemies = []
        self.previous_ticks = 0

    def getDeltaTime(self):
        self.t = pygame.time.get_ticks()
        self.deltaTime = (self.t-self.previous_ticks)
        self.previous_ticks = self.t

    def spawnEnemies(self):
        if(len(ENEMY_LIST)==0):
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullet = Bullet(int(self.SHIP.x + self.SHIP.width/2), self.SHIP.y-10, self.BULLET_IMG, 6)
                    self.SHIP.shoot(bullet)

    def action(self):
        self.SHIP.action()
        for e in self.enemies:
            e.move((self.WIDTH, self.HEIGHT))

    def shooting_handle(self):
        for i, b in enumerate(self.SHIP.ship_bullets):
            for j, e in enumerate(self.enemies):
                if b.Rect.colliderect(e.Rect):
                    del self.SHIP.ship_bullets[i]
                    del self.enemies[j]

    def draw(self):
        self.WIN.blit(self.BG_IMG, (0, 0))
        self.WIN.blit(self.SHIP.img, (self.SHIP.x, self.SHIP.y))
        for enemy in self.enemies:
            self.WIN.blit(enemy.img, (enemy.x, enemy.y))
        for bullet in self.SHIP.ship_bullets:
            self.WIN.blit(bullet.img, (bullet.x, bullet.y))
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
            self.spawnEnemies()
            self.key_manager()
            self.check_events()
            self.action()
            self.shooting_handle()
            self.draw()
        pygame.quit()

if __name__ == "__main__":
    GameManager().main()