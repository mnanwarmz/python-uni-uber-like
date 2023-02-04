class User:
    def __init__(self, userId, userEmail, userPassword, userName):
        self.id = userId
        self.email = userEmail
        self.password = userPassword
        self.name = userName

    def __str__(self):
        return "User: " + self.name + " (" + self.email + ")"
