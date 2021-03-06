"""
Gets the velocity if within 30 ft
from tower inputting the distance
"""
def velocityClose(distanceToTower):
    return 2.425 + 0.00175 * distanceToTower**2

"""
Gets the velocity if not within 30 ft
of tower inputting the distance
"""
def velocityFar(distanceToTower):
    return 0.625 + 0.12 * distanceToTower - 0.00025 * distanceToTower**2

"""
Gets the velocity depending on x and
if its within 30 ft of a tower
"""
def getVelocity(x):
    if x < 0:
        return 9999
    elif x < 30:
        return velocityClose(x)
    elif x < 470:
        return velocityFar(x)
    elif x < 530:
        return velocityClose(x)
    elif x < 970:
        return velocityFar(x)
    elif x < 1000:
        return velocityClose(x)
    else:
        return 9999

"""
Gets the nearest tower based on
the distance along the wire
"""
def getNearestTower(x):
    if x < 0:
        return "9999"
    elif x <= 250:
        return "first"
    elif x <= 750:
        return "middle"
    elif x <= 1000:
        return "end"
    else:
        return "9999"

"""
Gets the distance to nearest tower
based on which tower is passed in as 
well as the distance along the wire
"""
def getDistanceToTower(x, tower):
    if tower == "first":
        return x
    elif tower == "middle":
        return abs(500 - x)
    elif tower == "end":
        return 1000 - x
    else:
        return 9999

"""
Displays the tower, distance to tower
and velocity values
"""
def display(tower, dToTower, velocity):
    print("==========================================")
    print("The closest tower is the", tower)
    print("\nThe distance to the", tower, "tower is", dToTower, "ft")
    print("\nThe velocity of the cable car is", velocity, "ft/s")
    print("==========================================")

"""
Main calls the 'getNearestTower', 
'getDistanceToTower', 'getVelocity'
and 'display'
"""
def main():
    x = int(input("\nWhat is the distance along the wire?\n:"))
    tower = getNearestTower(x)
    dToTower = getDistanceToTower(x, tower)
    velocity = getVelocity(x)

    if(tower == "9999" or dToTower == 9999 or velocity == 9999):
        print("The number you entered is not on the wire.")
        return

    display(tower, dToTower, velocity)

main()

