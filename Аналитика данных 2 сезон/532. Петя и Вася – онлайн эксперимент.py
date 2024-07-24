N = int(input())
result = ["O", "P"]
wins = [0, 0]
for i in range(N - 1):
    result.extend(result)
    wins.extend(wins)
    for j in range(len(result)):
        if j < (len(result) + 1) // 2:
            result[j] += "O"
            if result[j][-2:] == "OO":
                wins[j] += 1
        else:
            result[j] += "P"
            if result[j][-2:] == "OP":
                wins[j] -= 1
V = len(list(filter(lambda s: s > 0, wins)))
P = len(list(filter(lambda s: s < 0, wins)))
N = len(list(filter(lambda s: s == 0, wins)))
print(P / len(result), N / len(result), V / len(result))