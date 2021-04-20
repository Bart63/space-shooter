import sys
import os
sys.path.insert(0, os.path.join('invaders'))
from Ship import Ship
import pygame

class GameManager:
    WIDTH, HEIGHT = 700, 700
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Space shooter")
    FPS = 60
    BG_IMG = pygame.image.load(os.path.join('imgs', 'background.png'))
    BG_IMG = pygame.transform.scale(BG_IMG, (WIDTH, HEIGHT))
    SHIP_IMG_PATH = os.path.join('imgs', 'gracz_new.png')

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False

    def draw(self, SHIP):
        self.WIN.blit(self.BG_IMG, (0, 0))
        self.WIN.blit(SHIP.img, (SHIP.x, SHIP.y))
        pygame.display.update()

    def main(self):
        SHIP = Ship(200, 200, self.SHIP_IMG_PATH)
        self.run = True
        clock = pygame.time.Clock()
        while self.run:
            clock.tick(self.FPS)
            self.check_events()
            self.draw(SHIP)
        pygame.quit()

if __name__ == "__main__":
    gm = GameManager()
    gm.main()