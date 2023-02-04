
print("Welcome to Uber-Like")
print("1. Sign Up")
print("2. Sign In")
print("3. Exit")

choice = int(input("Enter your choice: "))
while choice < 1 or choice > 2:
    print("Invalid choice")
    choice = int(input("Enter your choice: "))
if choice == 1:
    import auth.signup
if choice == 2:
    import auth.session
    import usermenu
if choice == 3:
    exit()
