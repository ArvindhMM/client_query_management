from auth import validate_login

username = input("Enter username: ")
password = input("Enter password: ")

role = validate_login(username, password)

if role:
    print(f"Login successful! Role = {role}")
else:
    print("Invalid username or password.")
