from Powerups.PowerUps import PowerUps

class FasterShooting(PowerUps):
    def __init__(self, is_active, duration, add_speed, ship):
        super(FasterShooting, self).__init__(is_active, duration)
        self.add_speed = add_speed
        self.ship = ship

    def activation(self):
        super().activation()
        self.speed = ship.speed

    def action(self):
        self.ship.speed = self.speed + self.add_speed
    
    def desactivation(self):
        super().desactivation()
        self.ship.speed = self.speed
