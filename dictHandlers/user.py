import dictHandlers.location as location
# Lists all the orders belonging to a user with the given ID


def userOrders(userId):
    f = open("resources/orders.txt", "r")
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    orders = []
    for line in lines:
        if userId == line.split(",")[1]:
            orderId = line.split(",")[0]
            userId = line.split(",")[1]
            pickupLocationId = line.split(",")[2]
            destinationId = line.split(",")[3]
            order = {
                "id": orderId,
                "userId": userId,
                "pickupLocation": location.locationName(pickupLocationId),
                "destination": location.locationName(destinationId)
            }
            # Appends the order to the orders array
            orders.append(order)
    f.close()

    if len(orders) == 0:
        return "No orders found"
    # Return the orders array
    return orders


# Displays the order history of a user with the given IDµ
def userHistory(userId):
    orders = userOrders(userId)
    for order in orders:
        print(order)


# Updates the name of a user with the given ID
def updateName(userId, name):
    f = open("resources/users.txt", "r")
    lines = f.readlines()
    for index, line in enumerate(lines):
        if userId == line.split(",")[0]:
            lines[index] = line.split(
                ",")[0] + "," + line.split(",")[1] + "," + line.split(",")[2] + "," + name + "\n"

    f.close()
    f = open("resources/users.txt", "w")
    f.writelines(lines)
    f.close()
