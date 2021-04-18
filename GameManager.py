import pygame
import os

class GameManager:
    WIDTH, HEIGHT = 700, 700
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Space shooter")
    FPS = 60
    BG_IMG = pygame.image.load(os.path.join('imgs', 'background.png'))
    BG_IMG = pygame.transform.scale(BG_IMG, (WIDTH, HEIGHT))

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False

    def draw(self):
        self.WIN.blit(self.BG_IMG, (0, 0))
        pygame.display.update()

    def main(self):
        self.run = True
        clock = pygame.time.Clock()
        while self.run:
            clock.tick(self.FPS)
            self.check_events()
            self.draw()
        pygame.quit()

if __name__ == "__main__":
    GameManager().main()