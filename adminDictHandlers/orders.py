from dictHandlers.location import locationName


def allOrders():
    """Returns all orders of the system"""
    f = open("resources/orders.txt", "r")
    lines = f.readlines()
    orders = []
    for line in lines:
        order = {
            "id": line.split(",")[0],
            "userId": line.split(",")[1],
            "pickupLocation": locationName(line.split(",")[2]),
            "destination": locationName(line.split(",")[3]),
        }
        # Append the order to the orders array
        orders.append(order)
    f.close()
    return orders


def removeOrder(orderId):
    """Removes an order from the system"""
    f = open("resources/orders.txt", "r")
    lines = f.readlines()
    f.close()
    f = open("resources/orders.txt", "w")
    for line in lines:
        if orderId != line.split(",")[0]:
            f.write(line)
    f.close()


def updateOrder(orderId, userId, pickupLocationId, destinationId):
    """Updates an order's information"""
    f = open("resources/orders.txt", "r")
    lines = f.readlines()
    f.close()
    f = open("resources/orders.txt", "w")
    for line in lines:
        if orderId == line.split(",")[0]:
            f.write(orderId + "," + userId + "," +
                    pickupLocationId + "," + destinationId + "\n")
        else:
            f.write(line)
    f.close()


def addOrder(userId, pickupLocationId, destinationId):
    """Adds a new order to the system"""
    f = open("resources/orders.txt", "r")
    lines = f.readlines()
    f.close()
    f = open("resources/orders.txt", "a")
    f.write(str(len(lines) + 1) + "," + userId + "," +
            pickupLocationId + "," + destinationId + "\n")
    f.close()
