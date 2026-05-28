from utils.storage import load_data, save_data
from utils.helpers import generate_id


class Auth:

    def login(self, username, password):

        data = load_data()

        for user in data.get("users", []):

            if user["username"] == username and user["password"] == password:
                return user

        return None


    def register(self, current_user, username, password, role):

        # CHECK ADMIN
        if current_user["role"] != "admin":
            print("Access Denied")
            return False

        data = load_data()

        # check duplicate user
        for user in data.get("users", []):

            if user["username"] == username:
                print("Username already exists")
                return False

        new_user = {
            "id": generate_id(data.get("users", []), "U"),
            "username": username,
            "password": password,
            "role": role
        }

        data["users"].append(new_user)

        save_data(data)
        print("User registered successfully!")

        return True

auth = Auth()
def register_menu(user):

    # ADMIN CHECK
    if user["role"] != "admin":
        print("Access Denied")
        return

    print("\n===== REGISTER USER =====")

    username = input("Username: ").strip()
    password = input("Password: ").strip()

    print("""
1. Admin
2. Teacher
3. Student
""")

    role_choice = input("Choose: ").strip()

    if role_choice == "1":
        role = "admin"

    elif role_choice == "2":
        role = "teacher"

    elif role_choice == "3":
        role = "student"

    else:
        print("Invalid role")
        return

    auth.register(
        user,
        username,
        password,
        role
    )