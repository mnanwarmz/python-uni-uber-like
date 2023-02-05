from auth.session import loggedInUser

print("Your User Profile")
print("ID: ", loggedInUser["id"])
print("Name: ", loggedInUser["name"])
print("Email: ", loggedInUser["email"])
print("Password: ", loggedInUser["password"])
