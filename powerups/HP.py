from Powerups.PowerUps import PowerUps

class HP(PowerUps):
    def __init__(self, is_active, duration, health_val):
        super(HP, self).__init__(is_active, duration)
        self.health_val = health_val

    def action(self, ship):
        ship.health += health_val