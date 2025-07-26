print("Simple Login System")
print("-------------------")

correct_username = "shree"
correct_password = "2807"

attempts = 3

while attempts > 0:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("Login successful!")
        break
    else:
        attempts -= 1
        print("Incorrect username or password.")
        if attempts > 0:
            print("Attempts remaining:", attempts)
        else:
            print("You have been blocked due to 3 failed attempts.")
