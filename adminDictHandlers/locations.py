def allLocations():
    # Read from locations.txt file
    f = open("resources/locations.txt", "r")
    lines = f.readlines()
    f.close()
    # Print all locations
    for line in lines:
        print(line.split(",")[0] + " " + line.split(",")[1])

def addLocation(locationName):
    # Read from locations.txt file
    f = open("resources/locations.txt", "r")
    lines = f.readlines()
    f.close()
    # Add new location to locations.txt file
    f = open("resources/locations.txt", "a")
    f.write(locationName + "\n")

def deleteLocation(locationId):
    # Read from locations.txt file
    f = open("resources/locations.txt", "r")
    lines = f.readlines()
    f.close()
    # Delete location from locations.txt file
    f = open("resources/locations.txt", "w")
    for line in lines:
        if line.split(",")[0] != locationId:
            f.write(line)
    f.close()

def updateLocation(locationId, locationName):
    # Read from locations.txt file
    f = open("resources/locations.txt", "r")
    lines = f.readlines()
    f.close()
    # Update location from locations.txt file
    f = open("resources/locations.txt", "w")
    for line in lines:
        if line.split(",")[0] != locationId:
            f.write(line)
        else:
            f.write(locationId + "," + locationName + "\n")
    f.close()