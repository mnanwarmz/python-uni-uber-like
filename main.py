# *********************************************************
# Program: TL15_G01.py
# Course: PSP0101 PROBLEM SOLVING AND PROGRAM DESIGN
# Tutorial Section: TL15 Group: G1
# Trimester: 2215
# Year: 2022/23 Trimester 1
# Member_1: 1221101160 | MUHAMMAD NABIL NAUFAL BIN MD ZAID
# Member_2: 1211112042 | GOH ROU LOU
# Member_3: 1221101048 | HABEBA NADER DEYAAEDDEIN EISA
# Member_4: 1221101167 | SIN YI WEI
# *********************************************************
# Task Distribution
# Member_1: GROUP LEADER, WROTE THE CODING, MADE FLOWCHARTS, WROTE THE DOCUMENTATION, CODE TESTER
# Member_2: WROTE THE CODING, CODE TESTER
# Member_3: MADE FLOWCHARTS, CODE TESTER
# Member_4: WROTE THE DOCUMENTATION, CODE TESTER
# *********************************************************

print("Welcome to Uber-Like")
print("1. Sign Up")
print("2. Sign In")
print("3. Exit")
# Requests user to enter a choice
choice = int(input("Enter your choice: "))
while choice < 1 or choice > 3:
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
