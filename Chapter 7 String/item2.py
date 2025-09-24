print(" *** Remove ODD characters ***")
s = input("Enter a string : ")

even_chars = ""
pos = 1
for ch in s:
    if pos % 2 == 0:
        even_chars += ch
    pos += 1

print("Even characters = " + even_chars)
print("===== End of program =====")
