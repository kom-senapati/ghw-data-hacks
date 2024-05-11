import bcrypt
import getpass
import json

LOGGED_IN = False

try:
    with open('users.json', 'r') as file:
        database = json.load(file)
except FileNotFoundError:
    database = {}

def save_to_json():
    with open('users.json', 'w') as file:
        json.dump(database, file, indent=4)

def register():
    username = input("Enter username: ")
    if username in database:
        print("Username already exists! 😕")
        return

    password = getpass.getpass("Enter password: ")
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    database[username] = str(hashed_password, 'utf-8')
    save_to_json()
    print("User registered successfully! 🎉")

def login():
    username = input("Enter username: ")
    if username not in database:
        print("User not found! 😕")
        return

    password = getpass.getpass("Enter password: ")
    hashed_password = database[username]

    if bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
        global LOGGED_IN
        LOGGED_IN = True
        print("Login successful! 🎉")
        home()
    else:
        print("Invalid password! 😕")

def home():
    if LOGGED_IN:
        print("Welcome to the home 🏠 page!")
    else:
        print("Please login to access the home page! 🔒")
        login()

def main():
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        print("4. Home")
        choice = input("Enter your choice: ")

        match choice:
            case '1':
                register()
            case '2':
                login()
            case '3':
                print("Exiting... 👋")
                break
            case '4':
                home()
            case _:
                print("Invalid choice! 😕")

if __name__ == "__main__":
    main()