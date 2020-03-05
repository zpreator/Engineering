import CableCarFunctions as funct

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
def getAndPrintData(x):
    
    # x = int(input("\nWhat is the distance along the wire?\n:"))
    
    tower = funct.getNearestTower(x)
    dToTower = funct.getDistanceToTower(x, tower)
    velocity = funct.getVelocity(x)
    if(tower == "9999" or dToTower == 9999 or velocity == 9999):
        print("The number you entered is not on the wire.")
        return

    display(tower, dToTower, velocity)

def main():
    loc = [260,530,995]
    [getAndPrintData(x) for x in loc]
    print("Wassup")

main()

