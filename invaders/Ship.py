from GlobalVars import WIDTH, HEIGHT, powerups, SHIP_WIDTH, SHIP_HEIGHT
from Invaders.Invaders import Invaders
from Weapons import Bullet, Explosion
from random import random, randint
import pygame

class Ship(Invaders):
    def __init__(self, x, y, image, movement_speed=1, shooting_speed=1, score=0, damage=1, health=100, 
                    width=SHIP_WIDTH, height=SHIP_HEIGHT, shooting_dir=(-1,0), right=0, down=0):
        super(Ship, self).__init__(x, y, image, score, movement_speed, damage, health, width, height, right, down)
        self.shooting_speed = shooting_speed
        self.shooting_dir = shooting_dir
        self.powerups = []

    def shoot(self):
        bullet = Bullet(int(self.x + self.width/2), self.y-10, direction=self.shooting_dir, speed=6)
        return bullet
        
    def move(self):
        keys_pressed = pygame.key.get_pressed()
        if (keys_pressed[pygame.K_d] or keys_pressed[pygame.K_RIGHT]) and self.x<WIDTH-self.width:
            self.right += 1
        if (keys_pressed[pygame.K_a] or keys_pressed[pygame.K_LEFT]) and self.x>0:
            self.right -= 1
        if (keys_pressed[pygame.K_s] or keys_pressed[pygame.K_DOWN]) and self.y<HEIGHT-self.height:
            self.down += 1
        if (keys_pressed[pygame.K_w] or keys_pressed[pygame.K_UP]) and self.y>0:
            self.down -= 1
        super().move()
        self.down = 0
        self.right = 0

    def action(self, deltaTime):
        for i, p in enumerate(self.powerups):
            p.check_time(deltaTime)
            if p.is_active:
                p.action()
            else:
                del self.powerups[i]
        super().action()
        if not self.is_alive:
            return Explosion(self.x, self.y, width=self.width, height=self.height)
        events = pygame.event.get(eventtype=pygame.KEYDOWN)
        for e in events:
            if e.key == pygame.K_SPACE and self.is_alive:
                return self.shoot()
            
    def get_score(self, points):
        self.score += points

    def get_powerup(self):
        if random()>0.9:
            powerup = powerups[randint(0, len(powerups)-1)](self)
            types = [type(p) for p in self.powerups]
            if type(powerup) in types:
                k = types.index(type(powerup))
                self.powerups[k].desactivation()
            self.powerups.append(powerup)