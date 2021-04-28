from Powerups.PowerUps import PowerUps

class HP(PowerUps):
    def __init__(self, ship, duration=500, is_active=False, health_val=9):
        super(HP, self).__init__(ship, duration, is_active)
        self.health_val = health_val

    def action(self):
        self.ship.health += self.health_val
        self.health_val = 0