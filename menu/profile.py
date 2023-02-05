# Imports the loggedInUser from the session
from auth.session import loggedInUser
# Imports the updateName function from the user.py file
from dictHandlers.user import updateName
print("Your User Profile")
print("ID: ", loggedInUser["id"])
print("Name: ", loggedInUser["name"])
print("Email: ", loggedInUser["email"])
print("Password: ", loggedInUser["password"])

print("Would you like to update your name? (Y/N)")
choice = input("Enter your choice: ")
if choice == "Y":
    print("Enter your new name")
    name = input("Enter your name: ")
    updateName(loggedInUser["id"], name)
    print("Your name has been updated successfully")
else:
    print("Thank you for using Uber-Like")
