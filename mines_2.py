import random
difficulty = input("Choose between Easy, Hard, Inhuman: ")

symbols = [1, 0]

n = 0

if difficulty == "Easy":
    n = 10
elif difficulty == "Hard":
    n = 20
elif difficulty == "Inhuman":
    n = 35
board = ""
for i in range(n):
    result = 0
    if difficulty == "Easy" or difficulty == "Hard":
        result = random.choices(symbols, weights=[50, 50], k=n)
    elif difficulty == "Inhuman":
        result = random.choices(symbols, weights=[50, 20], k=n)
    print(result)

print(board[0])

