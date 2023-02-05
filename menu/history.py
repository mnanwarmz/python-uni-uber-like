from auth.session import loggedInUser
from dictHandlers.user import userOrders
from dictHandlers.order import removeOrder
print("Order History")

orders = userOrders(loggedInUser["id"])
for order in orders:
    print(order)

print("Would you like to remove an order from your history? (y/n)")
choice = input("Enter your choice (e.g.: y): ")
while choice != "y" and choice != "n":
    print("Invalid choice")
    choice = input("Enter your choice (e.g.: y): ")

if choice == "y":
    removeOrder(input("Enter the ID of the order you would like to remove: "))
    print("Order removed successfully")

print("Updated Order History")
# Display the new updated history
orders = userOrders(loggedInUser["id"])
for order in orders:
    print(order)
