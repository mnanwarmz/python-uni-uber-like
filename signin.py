print("Login to the app")
email = input("Enter your email: ")
password = input("Enter your password: ")

# compare with resources/users.txt
# if email and password are correct
# then print("Welcome to Uber-Like")
# else print("Invalid Credentials")

f = open("resources/users.txt", "r")
lines = f.readlines()
auth = False
while auth == False:
    for index, line in enumerate(lines):
        if (email == line.split(",")[0] and password == line.split(",")[1]):
            auth = True
            print("Welcome to Uber-Like")
            break
        else:
            if index == len(lines) - 1:
                print("Invalid Credentials, Try Again")
                email = input("Enter your email: ")
                password = input("Enter your password: ")

f.close()
