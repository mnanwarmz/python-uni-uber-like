class Order:
    def __init__(self, orderId, userId, pickupLocationId, destinationId):
        self.id = orderId
        self.userId = userId
        self.pickupLocationId = pickupLocationId
        self.destinationId = destinationId

    def user(self):
        f = open("resources/users.txt", "r")
        lines = f.readlines()
        for line in lines:
            if self.userId == line.split(",")[0]:
                return line.split(",")[3]
        f.close()

    def pickup(self):
        f = open("resources/locations.txt", "r")
        lines = f.readlines()
        for line in lines:
            if self.pickupLocationId == line.split(",")[0]:
                return line.split(",")[1]
        f.close()

    def destination(self):
        f = open("resources/locations.txt", "r")
        lines = f.readlines()
        for line in lines:
            if self.destinationId == line.split(",")[0]:
                return line.split(",")[1]
        f.close()

    def __str__(self):
        return "Order Details: " + "User: " + self.user() + " Pickup Location: " + self.pickup() + " Destination: " + self.destination()