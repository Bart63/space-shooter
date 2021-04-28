from Powerups.PowerUps import PowerUps

class Invincibility(PowerUps):
    def __init__(self, is_active, duration):
        super(Invincibility, self).__init__(is_active, duration)
        
    def activation(self, ship):
        super().activation()
        self.health = ship.health

    def action(self, ship):
        ship.health = self.health