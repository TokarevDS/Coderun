n = int(input())
teams = input().split()
team = 0
for _ in range(n):
    if teams[team] == '-1':
        print('NO')
        break
    else:
        team = int(teams[team])
else:
    print('YES')