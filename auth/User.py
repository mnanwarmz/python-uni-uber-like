class User:
    def __init__(self, userId, userEmail, userPassword, userName):
        self.id = userId
        self.email = userEmail
        self.password = userPassword
        self.name = userName

    def __str__(self):
        return "User: " + self.name + " (" + self.email + ")"

    def orders(self):
        f = open("resources/orders.txt", "r")
        lines = f.readlines()
        userOrders = []
        for line in lines:
            if self.id == line.split(",")[1]:
                userOrders.append(line.split(",")[0])
        f.close()
        return userOrders