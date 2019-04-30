class SurfaceOcean():
    SURFACE_TO_ATMOSPHERE_RATE = 0.078111
    SURFACE_TO_DEEP_RATE = 0.10622

    def __init__(self, value):
        self.value = value

    def transferToAtmosphere(self):
        reduction = self.value * self.SURFACE_TO_ATMOSPHERE_RATE;
        self.value -= reduction
        return reduction

    def transferToDeep(self):
        reduction = self.value * self.SURFACE_TO_DEEP_RATE
        self.value -= reduction
        return reduction

    def acceptCarbon(self, value):
        self.value += value

    def getCarbonLevel(self):
        return self.value
