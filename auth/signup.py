print("Register Account")
name = input("Enter your name: ")
email = input("Enter your email: ")

# Check if the email is already registered
f = open("resources/users.txt", "r")
Lines = f.readlines()
emailInFile = True
while emailInFile == True:
    for line in Lines:
        if email in line:
            print("Email already registered")
        else:
            emailInFile = False
f.close()


passwordAccepted = False
while not passwordAccepted:
    password = input("Enter your password: ")
    if len(password) < 8:
        print("Password must be 8 characters long")
    else:
        passwordAccepted = True
        print("Account created successfully")


# Write the data in resources/users.txt
f = open("resources/users.txt", "a")
userId = len(Lines) + 1
f.write(str(userId)+","+email+","+password+","+name+"\n")
f.close()
