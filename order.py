print("Welcome to the Ordering Menu", "\n")

pickup_location = input("Where would like to be picked up?: ")
destination = input("Where would you like to go?: ")

LocationExist = True
f = open("resources/locations.txt", "r")
Lines = f.readlines()
while LocationExist == True:
    for line in Lines:
        if pickup_location in line:
            LocationExist = True
            break
        else:
            LocationExist = False
    f.close()
    if LocationExist == False:
        print(
            "Sorry, we do not have a driver in that area yet. Please try another location")
        pickup_location = input("Where would like to be picked up?: ")


DestinationExist = True
while DestinationExist == True:
    f = open("resources/locations.txt", "r")
    for line in f:
        if destination in line:
            DestinationExist = True
            break
        else:
            DestinationExist = False
    f.close()
    if DestinationExist == False:
        print(
            "Sorry, we do not have a driver in that area yet. Please try another location")
        destination = input("Where would you like to go?: ")

f = open("resources/rides.txt", "a")
f.write(pickup_location+","+destination+"\n")
f.close()
