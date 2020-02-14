import fluids.core as f
import thermo.chemical as c
import iapws.iapws97 as t

def getSpeedOfSoundInIdealGas(T, k, MW):
    return f.c_ideal_gas(T, k, MW)

def getChemical():
    co2 = c.Chemical('carbon dioxide')
    print(co2.formula)

def getH20TempAtPressure():
    steam = t.IAPWS97(T=80)
    print(steam.x)

getH20TempAtPressure()