from auth.signin import signin
import getpass

email = input("Enter your email: ")
password = getpass.getpass("Enter your password: ")

loggedInUser = signin(email, password)

print(str(loggedInUser))
