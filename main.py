
print("Welcome to Uber-Like")
print("1. Sign Up")
print("2. Sign In")
print("3. Exit")

choice = int(input("Enter your choice: "))
while choice < 1 or choice > 3:
    print("Invalid choice")
    choice = int(input("Enter your choice: "))
if choice == 1:
    import auth.signup
if choice == 2:
    import auth.session
    if auth.session.loggedInUser["role"] == "admin":
        import adminmenu
    if auth.session.loggedInUser["role"] == "user":
        import usermenu
if choice == 3:
    exit()
