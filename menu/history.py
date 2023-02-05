from auth.session import loggedInUser
from dictHandlers.user import userOrders
print("Order History")

orders = userOrders(loggedInUser["id"])
for order in orders:
    print(order)

