class Atmosphere():
    ATMOSPHERE_TO_SURFACE_RATE = 0.11915

    def __init__(self, value):
        self.value = value

    def transferToSurface(self):
        reduction = self.value * self.ATMOSPHERE_TO_SURFACE_RATE;
        self.value -= reduction
        return reduction

    def acceptCarbon(self, value):
        self.value += value

    def getCarbonLevel(self):
        return self.value
