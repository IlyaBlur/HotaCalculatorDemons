import math

import numpy as np
from numpy import *


Pitlords = int(input("Введите количество адских отродий: "))
Unit = int(input("Введите количество существ для демонения: "))
Xp = int(input("Введите количество хп одного существа: "))
UnitXP = Unit * Xp

PitlordsMAX = math.floor((Pitlords * 50) / 35)
UnitXPMAX = math.floor(UnitXP / 35)
demons = min(Unit, min(PitlordsMAX, UnitXPMAX))
print(demons)
