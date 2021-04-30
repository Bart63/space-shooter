from pygame import image as py_image, transform, Rect

class Invaders:
    def __init__(self, x, y, image, score, movement_speed=1, damage=1, health=100, width=100, height=100, 
                right=0, down=1):
        self.x = x
        self.y = y
        self.score = score
        self.health = health
        self.movement_speed = movement_speed
        self.damage = damage
        self.img = transform.scale(py_image.load(image), (width, height))
        self.width = width
        self.height = height
        self.down = down
        self.right = right
        self.Rect = Rect(self.x, self.y, self.width, self.height)
        self.is_alive = True

    def action(self):
        if self.health <= 0:
            self.die()
        else:
            self.move()

    def die(self):
        self.is_alive = False

    def move(self):
        self.x += self.right*self.movement_speed
        self.y += self.down*self.movement_speed
        self.Rect = Rect(self.x, self.y, self.width, self.height)

    def loose_health(self, damage):
        self.health -= int(damage)
        
    def is_colliding(self, obj) -> bool:
        return obj.Rect.colliderect(self.Rect)

    def check_collision(self, obj) -> bool:
        if self.is_colliding(obj):
            self.loose_health(obj.damage)
            return True
        return False

    def collision_handle(self, obj):
        res = []
        if type(obj) != list:
            obj = [obj]
        for o in obj:
            res.append(self.check_collision(o))
        return res