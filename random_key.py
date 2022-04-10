import random
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
nums = "1234567890"

keys = open("stupid_keys.txt", "w+")

combination = upper + lower + nums

key = 0

while True:
    result = "".join(random.choices(combination, k=10))
    key += 1
    if key > 100:
        break
    keys.write(f"{result}, ")
    print(f"{result},")
