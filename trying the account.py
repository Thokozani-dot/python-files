child = {
    "profile": {
        "academics": {
            "maths": None
        }
    },
    "account": None
}

def login(username, password):
    if child["account"] is None:
        print("This child does not have an account. Please register.")
        return

    if child["account"]["password"] != password:
        print("Wrong password. Please try again.")
        return

    print("Login successful!")

def register(username, password):
    child["account"] = {
        "username": username,
        "password": password
    }
    print("Registration successful!")
