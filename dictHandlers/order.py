# Remove an order from the orders.txt file based on their ID:
def removeOrder(orderId):
    f = open("resources/orders.txt", "r")
    lines = f.readlines()
    f.close()
    f = open("resources/orders.txt", "w")
    for line in lines:
        if orderId != line.split(",")[0]:
            f.write(line)
    f.close()
