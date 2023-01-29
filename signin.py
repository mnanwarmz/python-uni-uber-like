print("Login to the app")
email = input("Enter your email: ")
password = input("Enter your password: ")

# compare with accounts.txt
# if email and password are correct
# then print("Welcome to Uber-Like")
# else print("Invalid Credentials")

f = open("accounts.txt", "r")
lines = f.readlines()
auth = False
while auth == False:
    for line in lines:
        if (email == line.split(",")[0] and password == line.split(",")[1]):
            auth = True
            break
        else:
            print("Invalid Credentials, Try Again")
f.close()
