from adminDictHandlers.orders import *
from adminDictHandlers.locations import allLocations
print("Orders of the system")
orders = allOrders()
for order in orders:
    print(order)

print("Actions you can perform : ")
print("1. Remove an order")
print("2. Update an order")
print("3. Add a new order")

choice = int(input("Enter your choice (e.g.: 1): "))
while choice < 1 or choice > 3:
    print("Invalid choice")
    choice = int(input("Enter your choice: "))
if choice == 1:
    removeOrder(input("Enter the ID of the order you would like to remove: "))
    print("Order removed successfully")
if choice == 2:
    print("Locations of the system")
    allLocations()
    updateOrder(input("Enter the ID of the order you would like to update: "), input("Enter the new user ID of the order: "), input("Enter the new pickup location ID of the order: "), input("Enter the new destination ID of the order: "))
    print("Order updated successfully")
if choice == 3:
    print("Locations of the system")
    allLocations()
    addOrder(input("Enter the user ID of the order: "), input("Enter the pickup location ID of the order: "), input("Enter the destination ID of the order: "))
    print("Order added successfully")
