from Powerups.PowerUps import PowerUps

class Invincibility(PowerUps):
    def __init__(self, ship, duration=10, is_active=False):
        super(Invincibility, self).__init__(ship, duration, is_active)
        
    def activation(self):
        super().activation()
        self.health = self.ship.health

    def action(self):
        self.ship.health = self.health