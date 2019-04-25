import os
import sys
import math

parent_dir = os.path.abspath(os.path.dirname(__file__))
vendor_dir = os.path.join(parent_dir, 'vendor')

sys.path.append(vendor_dir)

import matplotlib.pyplot as plt

SURFACE_TO_DEEP_RATE = 0.10622
DEEP_TO_SURFACE_RATE = 0.0025768

ATMOSPHERE_TO_SURFACE_RATE = 0.11915
SURFACE_TO_ATMOSPHERE_RATE = 0.078111

INITIAL_MASS_ATMOSPHERE = 590
INITIAL_MASS_SURFACE = 900
INITIAL_MASS_DEEP = 37100

dt = 1

years = [1750]

atmosphereCarbon = [INITIAL_MASS_ATMOSPHERE]
surfaceCarbon = [INITIAL_MASS_SURFACE]
deepCarbon = [INITIAL_MASS_DEEP]


def getChangeInAtmosphericCarbon():
    return currentSurfaceCarbon * SURFACE_TO_ATMOSPHERE_RATE - currentAtmosphereCarbon * ATMOSPHERE_TO_SURFACE_RATE

def getChangeInSurfaceCarbon():
    return (currentAtmosphereCarbon * ATMOSPHERE_TO_SURFACE_RATE + currentDeepCarbon * DEEP_TO_SURFACE_RATE
            -
            (currentSurfaceCarbon * SURFACE_TO_DEEP_RATE + currentSurfaceCarbon * SURFACE_TO_ATMOSPHERE_RATE))

def getChangeInDeepCarbon():
    return currentSurfaceCarbon * SURFACE_TO_DEEP_RATE - currentDeepCarbon * DEEP_TO_SURFACE_RATE


while years[-1] < 2019:
    currentAtmosphereCarbon = atmosphereCarbon[-1]
    currentSurfaceCarbon = surfaceCarbon[-1]
    currentDeepCarbon = deepCarbon[-1]

    newAtmosphereCarbon = currentAtmosphereCarbon + getChangeInAtmosphericCarbon()
    newSurfaceCarbon = currentSurfaceCarbon + getChangeInSurfaceCarbon()
    newDeepCarbon = currentDeepCarbon + getChangeInDeepCarbon()

    atmosphereCarbon.append(newAtmosphereCarbon)
    surfaceCarbon.append(newSurfaceCarbon)
    deepCarbon.append(newDeepCarbon)

    years.append(years[-1] + dt)

plt.plot(years, atmosphereCarbon, 'r-', years, surfaceCarbon, 'b-', years, deepCarbon, 'g-')
plt.legend(['Atmospheric Carbon', 'Surface Ocean Carbon', 'Deep Ocean Carbon'])
plt.xlabel('Year')
plt.ylabel('Carbon (PgC)')
plt.show()
