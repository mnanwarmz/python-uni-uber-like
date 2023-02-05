from adminDictHandlers.locations import *
def locations():
    print("Welcome to Uber-Like")
    print("Listed below is a list of the locations we currently serve")

    # Read from locations.txt file
    f = open("resources/locations.txt", "r")
    lines = f.readlines()
    for line in lines:
        print(line)
    f.close()

    print("Enter your desired action")
    print("1. Add a location")
    print("2. Delete a location")
    print("3. Change a location's name")
    print("4. Return to admin menu")

    choice = int(input("Enter your choice (e.g.: 1): "))
    while choice < 1 or choice > 3:
        print("Invalid choice")
        choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Enter the name of the location you would like to add")
        addLocation("locationName")
    if choice == 2:
        locationId = input("Enter the id of the location you would like to delete: ")
        # If not available, print "Location not found"
        if locationId in lines:
            deleteLocation(locationId)
        else:
            print("Location not found")
    if choice == 3:
        locationId = input("Enter the id of the location you would like to change: ")
        # If not available, print "Location not found"
        if locationId in lines:
            updateLocation(locationId, input("Enter the new name of the location: "))
        else:
            print("Location not found")
    if choice == 4:
        import adminmenu

    # after user makes their choice return them to this page
    import adminmenu