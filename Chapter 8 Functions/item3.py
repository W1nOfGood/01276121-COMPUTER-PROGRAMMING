print(" *** Recite the multiplication table ***")
tokens = input("Enter pattern for child 1 to 3 (-1 for sep) : ").split()

patterns = []
current = []
sep_count = 0
for t in tokens:
    if t == "-1":
        patterns.append(current)
        current = []
        sep_count += 1
        if sep_count == 3:
            break
    else:
        current.append(int(t))

p1, p2, p3 = patterns[0], patterns[1], patterns[2]

print()
def pat_str(p):
    return " ".join(str(x) for x in p) + " "

print("Pattern for child 1 : " + pat_str(p1))
print("Pattern for child 2 : " + pat_str(p2))
print("Pattern for child 3 : " + pat_str(p3))

ans = 0
for day in range(1, 366):
    a = p1[(day - 1) % len(p1)]
    b = p2[(day - 1) % len(p2)]
    c = p3[(day - 1) % len(p3)]
    if a == b and b == c:
        ans = day
        break

if ans != 0:
    print("They recite same multiplication table in " + str(ans) + " days")
else:
    print("This year they never recite same multiplication table !!!")
