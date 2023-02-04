from auth.User import User
print("Login to the app")
# compare with resources/users.txt
# if email and password are correct
# then print("Welcome to Uber-Like")
# else print("Invalid Credentials")


def signin(email, password):
    f = open("resources/users.txt", "r")
    lines = f.readlines()
    auth = False
    while auth == False:
        for index, line in enumerate(lines):
            if (email == line.split(",")[1] and password == line.split(",")[2]):
                auth = True
                userId = line.split(",")[0]
                userEmail = line.split(",")[1]
                userPassword = line.split(",")[2]
                userName = line.split(",")[3]
                user = User(userId, userEmail,
                            userPassword, userName)
                print("Welcome to Uber-Like")
                return user
            else:
                if index == len(lines) - 1:
                    print("Invalid Credentials, Try Again")
                    email = input("Enter your email: ")
                    password = input("Enter your password: ")

    f.close()
