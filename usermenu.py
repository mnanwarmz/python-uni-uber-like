print("Welcome to Uber-Like")
print("Listed below is a list of the locations we currently serve")

# Read from locations.txt file
f = open("resources/locations.txt", "r")
lines = f.readlines()
for line in lines:
    print(line)
f.close()

print("Enter your desired action")
print("1. Order a ride")
print("2. View your ride history")
print("3. View your profile")
print("4. Sign out")

choice = int(input("Enter your choice (e.g.: 1): "))
while choice < 1 or choice > 4:
    print("Invalid choice")
    choice = int(input("Enter your choice: "))

if choice == 1:
    import menu.order
if choice == 2:
    import menu.history
if choice == 3:
    import profile
if choice == 4:
    import main
