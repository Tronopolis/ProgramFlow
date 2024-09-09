name = input("Please enter your name: ")
age = int(input("How old are you, {0}? ".format(name)))

if 18 <= age < 31:
    print("Welcome to the holiday")
else:
    print("Sorry, you are not eligible for the holiday")
