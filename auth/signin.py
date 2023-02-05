print("Login to the app")
# compare with resources/users.txt
# if email and password are correct
# then print("Welcome to Uber-Like")
# else print("Invalid Credentials")


def signin(email, password):
    # Check both files for the user
    # admins.txt has the admin users
    for filename in ['resources/admins.txt', 'resources/users.txt']:
        with open(filename, "r") as f:
            lines = f.readlines()
            for line in lines:
                if (email == line.split(",")[1] and password == line.split(",")[2]):
                    userId = line.split(",")[0]
                    userEmail = line.split(",")[1]
                    userPassword = line.split(",")[2]
                    userName = line.split(",")[3]
                    # Assign roles according to their file
                    role = "admin" if filename == 'resources/admins.txt' else "user"
                    user = {
                        "id": userId,
                        "email": userEmail,
                        "password": userPassword,
                        "name": userName,
                        "role": role
                    }
                    print("Welcome to Uber-Like")
                    return user

    print("Invalid Credentials, Try Again")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    return signin(email, password)
