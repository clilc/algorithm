n = int(input())
plans = input().split(" ")
x, y = 1, 1

dx = [-1, 1, 0, 0] # L R U D
dy = [0, 0, -1, 1]
move_types = ["L", "R", "U", "D"]

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = x + dy[i]
        
    if nx <1 or ny <1 or nx > n or ny > n:
        continue

    x , y = nx , ny

print(x, y)
            