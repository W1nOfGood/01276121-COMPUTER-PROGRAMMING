print(" *** Center-starting Spiral Rectangle ***")
raw = input("Enter side direction: ")

parts = raw.split()
n = int(parts[0])
dirword = parts[1].lower()
start = 1
if len(parts) >= 3:
    start = int(parts[2])

grid = []
i = 0
while i < n:
    grid.append([0] * n)
    i += 1

if n % 2 == 0:
    r = n // 2 - 1
    c = n // 2 - 1
else:
    r = n // 2
    c = n // 2

dr = [-1, 0, 1, 0]
dc = [ 0, 1, 0,-1]
didx = 0
if dirword == "up":
    didx = 0
elif dirword == "right":
    didx = 1
elif dirword == "down":
    didx = 2
else:
    didx = 3

cur = start
end = start + n*n - 1
grid[r][c] = cur
step_len = 1
while cur < end:
    t = 0
    while t < 2 and cur < end:
        s = 0
        while s < step_len and cur < end:
            r = r + dr[didx]
            c = c + dc[didx]
            cur += 1
            grid[r][c] = cur
            s += 1
        didx = didx + 1
        if didx == 4:
            didx = 0
        t += 1
    step_len += 1

width = len(str(end))

row = 0
while row < n:
    col = 0
    line = ""
    while col < n:
        val = grid[row][col]
        fmt = "{:>" + str(width) + "d} "
        line += fmt.format(val)
        col += 1
    print(line)
    row += 1

print("===== End of program ======")
