# for i in range(10):
#     print("i is now {}".format(i))

# i=0
# while i<10:
#     print("i is now {}".format(i))
#     i+=1

for i in range(21):
    if (i % 3 == 0) or (i % 5 == 0):
        continue
    print(i)