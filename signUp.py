import userUpdater

print("Welcome to Efe's Flight Club.\n \
We find the best flight deals and email them to you.")

first_name = input("What is your first name? ").title()
last_name = input("What is your last name? ").title()

email1 = input("What is you email? ")
email2 = input("Please verify your email: ")
while email1 != email2:
    email1 = input("What is your email? ")
    if email1.lower() == "quit" or email1.lower() == "exit":
        exit()
    email2 = input("Please verify your email: ")
    if email2.lower() == "quit" or email2.lower() == "exit":
        exit()

print("OK. You're in the club!")

userUpdater.post_new_row(first_name, last_name, email1)
