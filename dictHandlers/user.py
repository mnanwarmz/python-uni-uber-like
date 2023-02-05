import dictHandlers.location as location
def userOrders(userId):
    f = open("resources/orders.txt", "r")
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    orders = []
    for line in lines:
        print(line.split(","))
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
            orders.append(order)
    f.close()
    return orders

def userHistory(userId):
    orders = userOrders(userId)
    for order in orders:
        print(order)