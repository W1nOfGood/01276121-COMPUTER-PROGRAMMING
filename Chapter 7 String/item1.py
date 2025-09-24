print(" *** Adding number ***")
words = input("Enter your words : ").split()

i = 1
for w in words:
    if i % 2 == 0:
        rev = ""
        for ch in w:
            rev = ch + rev
        print(rev + str(i), end=" ")
    else:
        print(w + str(i), end=" ")
    i += 1

print("\n==== End of program =====")
