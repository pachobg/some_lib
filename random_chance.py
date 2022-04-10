import random
bomb = "*"
empty = "-"
bonus = "@"
n = 20
combination = bomb + empty + bonus

random_1 = " ".join(random.choices(combination, weights=[100, 5, 5], k=n))
random_2 = " ".join(random.choices(combination, weights=[10, 100, 20], k=n))
random_3 = " ".join(random.choices(combination, weights=[5, 5, 5], k=n))
print(random_1)
print()
print(random_2)
print()
print(random_3)
