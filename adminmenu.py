print("Welcome to Uber-Like")

print("Enter your desired action")
print("1. View users")
print("2. View orders")
print("3. View locations")
print("4. Sign out")

choice = int(input("Enter your choice (e.g.: 1): "))
while choice < 1 or choice > 4:
    print("Invalid choice")
    choice = int(input("Enter your choice: "))

if choice == 1:
    import adminMenu.users
if choice == 2:
    import adminMenu.orders
if choice == 3:
    import adminMenu.locations
if choice == 4:
    print("You have been signed out")
    print("Thank you for using Uber-Like")
    exit()