print("Welcome to Uber-Like")
print("Listed below is a list of the locations we currently serve")

# Read from locations.txt file
f = open("locations.txt", "r")
lines = f.readlines()
for line in lines:
    print(line)
f.close()

print("Enter your desired action")
print("1. Order a ride")
print("2. View your ride history")
print("3. View your profile")
print("4. Sign out")

choice = int(input("Enter your choice: "))
if choice == 1:
    import order
elif choice == 2:
    import history
elif choice == 3:
    import profile
elif choice == 4:
    import main
else:
    print("Invalid Choice")
