user_first_name = input("What is your first name?\n")
user_last_name = input("What is your last name?\n")

user_full_name = user_first_name + " " + user_last_name

print(f"So your full name is {user_full_name}?\n")

print("The code from here on is done from my desktop!\n")

num = input("Guess a number 1-10!\n")
correct_num = 8

if num == "8":
    print("That's right!\n")
else:
    print("Nope!\n")