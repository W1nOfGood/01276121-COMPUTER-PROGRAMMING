print(" *** Transform to seconds ***")
a, b, c = input("Enter h m s : ").split()
a = int(a)
b = int(b)
c = int(c)

th = a*60*60
bh = b*60

total = th + bh + c

print(f"{a} hours {b} minutes {c} seconds = {total:,} seconds")
print("===== End of program =====")