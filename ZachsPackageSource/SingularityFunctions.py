def ConcentratedMoment(x, a):
    """ <x-a>^-2 """
    if x == a:
        return 1e9
    else:
        return 0

def ConcentratedForce(x, a):
    """ <x-a>^-1 """
    if x != a:
        return 0
    else:
        return 1e9

def UnitStep(x, a):
    """ <x-a>^0 """
    if x < a:
        return 0
    else:
        return 1

def Ramp(x, a):
    """ <x-a>^1 """
    if x < a:
        return 0
    else:
        return x-a