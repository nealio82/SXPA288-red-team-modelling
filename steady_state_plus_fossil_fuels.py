import os
import sys
import math

parent_dir = os.path.abspath(os.path.dirname(__file__))
vendor_dir = os.path.join(parent_dir, 'vendor')
model_dir = os.path.join(parent_dir, 'Model')

sys.path.append(vendor_dir)
sys.path.append(model_dir)

import matplotlib.pyplot as plt

from Atmosphere import Atmosphere
from DeepOcean import DeepOcean
from SurfaceOcean import SurfaceOcean

INITIAL_MASS_ATMOSPHERE = 590
INITIAL_MASS_SURFACE = 900
INITIAL_MASS_DEEP = 37100

dt = 1

years = [1750]

atmosphere = Atmosphere(INITIAL_MASS_ATMOSPHERE)
surface = SurfaceOcean(INITIAL_MASS_SURFACE)
deep = DeepOcean(INITIAL_MASS_DEEP)

atmosphereCarbon = [atmosphere.getCarbonLevel()]
surfaceCarbon = [surface.getCarbonLevel()]
deepCarbon = [deep.getCarbonLevel()]

def burningOfFossilFuels(year):
    return (10 ** -26) * math.exp(0.0345 * year)

while years[-1] < 2019:
    atmosphere.acceptCarbon(surface.transferToAtmosphere())
    surface.acceptCarbon(atmosphere.transferToSurface())
    surface.acceptCarbon(deep.transferToSurface())
    deep.acceptCarbon(surface.transferToDeep())

    atmosphere.acceptCarbon(burningOfFossilFuels(years[-1]))

    atmosphereCarbon.append(atmosphere.getCarbonLevel())
    surfaceCarbon.append(surface.getCarbonLevel())
    deepCarbon.append(deep.getCarbonLevel())

    years.append(years[-1] + dt)

plt.plot(years, atmosphereCarbon, 'r-', years, surfaceCarbon, 'b-', years, deepCarbon, 'g-')
plt.legend(['Atmospheric Carbon', 'Surface Ocean Carbon', 'Deep Ocean Carbon'])
plt.xlabel('Year')
plt.ylabel('Carbon (PgC)')
plt.show()
