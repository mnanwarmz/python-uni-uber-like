print("Register Account")
name = input("Enter your name: ")
email = input("Enter your email: ")
password = input("Enter your password: ")

# Write the data in users.txt
f = open("accounts.txt", "a")
f.write(email+","+password+","+name+"\n")
f.close()
