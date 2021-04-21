import os
from Invaders import Ship
from Weapons import Bullet
import pygame

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
        self.SHIP = Ship(self.WIDTH/2, self.HEIGHT-80, self.SHIP_IMG_PATH, 2)
        self.run = True
        self.ship_bullets = []
        self.enemies = []

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullet = Bullet(int(self.SHIP.x + self.SHIP.width/2), self.SHIP.y-10, self.BULLET_IMG, 3)
                    self.ship_bullets.append(bullet)

    def handle_bullets(self):
        for i, bullet in enumerate(self.ship_bullets):
            bullet.move(-1)
            if(bullet.y+bullet.height<0):
                del self.ship_bullets[i]

    def draw(self):
        self.WIN.blit(self.BG_IMG, (0, 0))
        self.WIN.blit(self.SHIP.img, (self.SHIP.x, self.SHIP.y))
        for bullet in self.ship_bullets:
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
            self.key_manager()
            self.check_events()
            self.handle_bullets()
            self.draw()
        pygame.quit()

if __name__ == "__main__":
    GameManager().main()