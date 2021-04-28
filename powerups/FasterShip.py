from Powerups.PowerUps import PowerUps

class FasterShip(PowerUps):
    def __init__(self, ship, duration=5000, is_active=False, add_speed=1):
        super(FasterShip, self).__init__(ship, duration, is_active)
        self.base_speed = ship.movement_speed
        self.add_speed = add_speed

    def activation(self):
        super().activation()
        self.ship.movement_speed = self.base_speed + self.add_speed
    
    def desactivation(self):
        print("Koniec")
        self.ship.movement_speed = self.base_speed
        super().desactivation()
