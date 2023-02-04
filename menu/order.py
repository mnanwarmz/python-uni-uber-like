from auth.session import loggedInUser
print("Welcome to the Ordering Menu", "\n")

pickupLocationId = input("Where would like to be picked up [Enter ID of Location]?: ")
destinationId = input("Where would you like to go? [Enter ID of Location]: ")

locationExist = False
f = open("resources/locations.txt", "r")
lines = f.readlines()
while locationExist == False :
    for index, line in enumerate(lines):
        if pickupLocationId in line:
            locationExist = True
            break
    if index == len(lines) - 1:
        print(
            "Sorry, we do not have a driver in that area yet. Please try another location")
        pickupLocationId = input("Where would you like to be picked up?: ")

f.close()


DestinationExist = False
while DestinationExist == False:
    f = open("resources/locations.txt", "r")
    lines = f.readlines()
    for index, line in enumerate(lines):
        if destinationId in line:
            DestinationExist = True
            break
    if index == len(lines) - 1:
        print(
            "Sorry, we do not have a driver in that area yet. Please try another location")
        destinationId = input("Where would you like to go?: ")

    f.close()


f = open("resources/orders.txt", "r")
lines = f.readlines()
f.close()
f = open("resources/orders.txt", "a")
orderId = len(lines) + 1
f.write(str(orderId) + "," + str(loggedInUser.id) + "," + str(pickupLocationId) + "," + str(destinationId) + " \r ")
f.close()

print("Your ride has been ordered successfully")
print("Pickup Location: ", pickupLocationId)
print("Destination: ", destinationId)
