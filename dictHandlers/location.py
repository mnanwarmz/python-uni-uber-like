def locationName(locationId):
    f = open("resources/locations.txt", "r")
    lines = f.readlines()
    for index,line in enumerate(lines):
        if locationId == line.split(",")[0]:
            return line.split(",")[1]
        else:
            if index == len(lines) - 1:
                return "Location not found"
    f.close()
