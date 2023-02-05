from auth.session import loggedInUser
from dictHandlers.location import locationName

print("Welcome to the Ordering Menu", "\n")

# Gets user input for pickup location and destination
pickupLocationId = input(
    "Where would like to be picked up [Enter ID of Location]?: ")
destinationId = input("Where would you like to go? [Enter ID of Location]: ")

# Flag to check if the location exists
locationExist = False
# Opens the locations.txt file in read mode
f = open("resources/locations.txt", "r")
# Parses the file line by line
lines = f.readlines()
while locationExist == False:
    for index, line in enumerate(lines):
        if pickupLocationId in line:
            locationExist = True
            break
        else:
            # If by the end of the file the location is not found, the user is asked to enter a new location
            if index + 1 == len(lines):
                print(
                    "Sorry, we do not have a driver in that area yet. Please try another location")
                pickupLocationId = input(
                    "Where would you like to be picked up?: ")

f.close()

# Flag to check if the location exists

DestinationExist = False
while DestinationExist == False:
    # Opens the locations.txt file in read mode
    f = open("resources/locations.txt", "r")
    lines = f.readlines()
    # Parses the file line by line
    for index, line in enumerate(lines):
        if destinationId in line:
            DestinationExist = True
            break
        else:
            # If by the end of the file the location is not found, the user is asked to enter a new location
            if index + 1 == len(lines):
                print(
                    "Sorry, we do not have a driver in that area yet. Please try another location")
                destinationId = input("Where would you like to go?: ")

    f.close()

f = open("resources/orders.txt", "r")
lines = f.readlines()
f.close()
# Opens the orders.txt file in append mode
f = open("resources/orders.txt", "a")
# Gets the number of lines in the file and adds 1 to it to get the order id
orderId = len(lines) + 1
f.write(str(orderId) + "," + str(loggedInUser["id"]) + "," + str(
    pickupLocationId) + "," + str(destinationId) + "\n")
f.close()

print("Your ride has been ordered successfully")
print("Pickup Location: ", locationName(pickupLocationId))
print("Destination: ", locationName(destinationId))
