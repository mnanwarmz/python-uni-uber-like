
print("Welcome to Uber-Like")
print("1. Sign Up")
print("2. Sign In")
print("3. Exit")
# Requests user to enter a choice
choice = int(input("Enter your choice: "))
while choice < 1 or choice > 2:
    print("Invalid choice")
    choice = int(input("Enter your choice: "))
if choice == 1:
    # Moves to the signup.py file to display the signup page
    import auth.signup
if choice == 2:
    # Moves to the signin.py file to display the signin page
    import auth.session
    if auth.session.loggedInUser["role"] == "admin":
        # Displays the admin menu if the user is an admin
        import adminmenu
    if auth.session.loggedInUser["role"] == "user":
        # Displays the user menu if the user is a user
        import usermenu
if choice == 3:
    exit()
