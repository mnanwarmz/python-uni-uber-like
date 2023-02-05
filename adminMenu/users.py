from adminDictHandlers.users import *
print("Users of the system")
users = allUsers()
for user in users:
    print(user)

print("Actions you can perform : ")
print("1. Remove a user")
print("2. Update a user's name")
print("3. View a user's order history")
print("4. Add a new User")

choice = int(input("Enter your choice (e.g.: 1): "))
while choice < 1 or choice > 4:
    print("Invalid choice")
    choice = int(input("Enter your choice: "))
if choice == 1:
    removeUser(input("Enter the ID of the user you would like to remove: "))
    print("User removed successfully")
if choice == 2:
    updateUser(input("Enter the ID of the user you would like to update: "), input("Enter the new email of the user: "), input("Enter the new name of the user: "))
    print("User updated successfully")
if choice == 3:
    userHistory(input("Enter the ID of the user you would like to view the history of: "))
if choice == 4:
    addUser(input("Enter the email of the admin: "),input("Enter the password of the admin"), input("Enter the name of the admin: "))
    print("User added successfully")

import adminmenu