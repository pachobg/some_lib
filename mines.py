import random

difficulty = input("Choose between Easy, Hard, Inhuman or Custom: ")

n = 0
k = 0
if difficulty == "Easy":
    n = 10
elif difficulty == "Hard":
    n = 25
elif difficulty == "Inhuman":
    n = 50
elif difficulty == "Custom":
    n = int(input("Enter first number: "))
    k = int(input("Enter second number "))
bomb = "*"
empty = "-"
combinations = bomb + empty
board = ""

for i in range(n):
    if difficulty == "Easy":
        board = " ".join(random.choices(combinations, weights=[15, 50], k=n))

    elif difficulty == "Hard":
        board = " ".join(random.choices(combinations, weights=[25, 50], k=n))

    elif difficulty == "Inhuman":
        board = " ".join(random.choices(combinations, weights=[50, 50], k=n))

    elif difficulty == "Custom":
        board = " ".join(random.choices(combinations, weights=[35, 50], k=k))
    print(board)

print()

# player_board

if difficulty == "Easy" or difficulty == "Hard" or difficulty == "Inhuman":
    for i in range(n):
        for j in range(n):
            print("^ ", end="")
        print()
elif difficulty == "Custom":
    for i in range(n):
        for j in range(k):
            print("^ ", end="")
        print()

number_of_guesses = 10
lives = 3
