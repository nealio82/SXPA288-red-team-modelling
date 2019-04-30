import os
import sys

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

while years[-1] < 2019:
    atmosphere.acceptCarbon(surface.transferToAtmosphere())
    surface.acceptCarbon(atmosphere.transferToSurface())
    surface.acceptCarbon(deep.transferToSurface())
    deep.acceptCarbon(surface.transferToDeep())

    atmosphereCarbon.append(atmosphere.getCarbonLevel())
    surfaceCarbon.append(surface.getCarbonLevel())
    deepCarbon.append(deep.getCarbonLevel())

    years.append(years[-1] + dt)

plt.plot(years, atmosphereCarbon, 'r-', years, surfaceCarbon, 'b-', years, deepCarbon, 'g-')
plt.legend(['Atmospheric Carbon', 'Surface Ocean Carbon', 'Deep Ocean Carbon'])
plt.xlabel('Year')
plt.ylabel('Carbon (PgC)')
plt.show()


# 1959 315.98,
# 1960 316.91,
# 1961 317.64,
# 1962 318.45,
# 1963 318.99,
# 1965 320.04,
# 1966 321.38,
# 1967 322.16,
# 1968 323.05,
# 1969 324.63,
# 1970 325.68,
# 1971 326.32,
# 1972 327.45,
# 1973 329.68,
# 1974 330.25,
# 1975 331.15,
# 1976 332.15,
# 1977 333.90,
# 1978 335.51,
# 1979 336.85,
# 1980 338.69,
# 1981 339.93,
# 1982 341.13,
# 1983 342.78,
# 1984 344.42,
# 1985 345.90,
# 1986 347.15,
# 1987 348.93,
# 1988 351.48,
# 1989 352.91,
# 1990 354.19,
# 1991 355.59,
# 1992 356.37,
# 1993 357.04,
# 1994 358.89,
# 1995 360.88,
# 1996 362.64,
# 1997 363.76,
# 1998 366.63,
# 1999 368.31,
# 2000 369.48,
# 2001 371.02,
# 2002 373.10,
# 2003 375.64,
# 2004 377.38,
# 2005 379.67,
# 2006 381.84,
# 2007 383.55,
# 2008 385.34