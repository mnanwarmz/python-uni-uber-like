from dictHandlers.user import userOrders
def allUsers():
    """Returns a list of all users in the system."""
    f = open("resources/users.txt", "r")
    lines = f.readlines()
    users = []
    for line in lines:
        user = {
            "id": line.split(",")[0],
            "email": line.split(",")[1],
            "Name": line.split(",")[3]
        }
        users.append(user)
    f.close()
    return users

def removeUser(userId):
    """Removes a user from the system."""
    f = open("resources/users.txt", "r")
    lines = f.readlines()
    for index,line in enumerate(lines):
        if userId == line.split(",")[0]:
            del lines[index]
    f.close()
    f = open("resources/users.txt", "w")
    f.writelines(lines)
    f.close()

def updateUser(userId, email, name):
    """Updates a user's information."""
    f = open("resources/users.txt", "r")
    lines = f.readlines()
    for index,line in enumerate(lines):
        if userId == line.split(",")[0]:
            lines[index] = line.split(",")[0] + "," + email + "," + line.split(",")[2] + "," + name + "\n"
    f.close()
    f = open("resources/users.txt", "w")
    f.writelines(lines)
    f.close()

def addUser(email, password, name):
    """Adds a new user to the system."""
    f = open("resources/admins.txt", "r")
    lines = f.readlines()
    f.close()
    f = open("resources/admins.txt", "a")
    f.write(str(len(lines) + 1) + "," + email + "," + password + "," + name + "\n")
    f.close()

def userHistory(userId):
    """Prints a user's order history."""
    orders = userOrders(userId)
    for order in orders:
        print(order)
