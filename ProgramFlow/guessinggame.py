import random
highest = 10
answer = random.randint(1, highest)
print(answer) # TODO: Remove after testing
print("Please guess number between 1 and {}: ".format(highest))

guess = int(input())

while guess != answer:
    if guess == 0:
        break
    if guess < answer:
        print("Please guess higher")
    elif guess > answer:
        print("Please guess lower")
    guess = int(input())

if guess == answer:
    print("Well done, you guessed it")
else:
    print("Sorry, you have not guessed correctly")



