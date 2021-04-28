class PowerUps:
    def __init__(self, is_active, duration):
        self.is_active = is_active
        self.duration = duration

    def action(self, ship):
        pass

    def check_time(self, delta_time):
        if self.is_active:
            self.duration -= delta_time
            if self.duration <= 0:
                self.desactivation()
        elif self.duration>0:
            self.is_active = True
            self.activation()

    def activation(self):
        self.is_active = True

    def desactivation(self):
        self.is_active = False