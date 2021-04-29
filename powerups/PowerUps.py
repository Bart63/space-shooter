class PowerUps:
    def __init__(self, ship, duration, is_active=False):
        self.is_active = is_active
        self.duration = duration
        self.ship = ship

    def action(self):
        pass

    def check_time(self, delta_time):
        if self.is_active:
            self.duration -= delta_time
            if self.duration <= 0:
                self.desactivation()
        elif self.duration > 0:
            self.is_active = True
            self.activation()

    def activation(self):
        self.is_active = True

    def desactivation(self):
        self.duration = 0
        self.is_active = False