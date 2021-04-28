from Powerups.PowerUps import PowerUps

class Shield(PowerUps):
    def __init__(self, ship, duration=5000, is_active=False):
        super(Shield, self).__init__(ship, duration, is_active)
        
    def activation(self):
        super().activation()
        self.health = self.ship.health

    def action(self):
        if self.ship.health<=self.health:
            self.ship.health = self.health