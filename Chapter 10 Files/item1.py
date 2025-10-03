print(" *** Find Total lines ***")
fname = input("Enter file name : ")

fhand = open(fname, "r", encoding="UTF-8")
print("property =>", fhand)

count = 0
for line in fhand:
    count = count + 1

num = str(count)
result = ""
while len(num) > 3:
    result = "," + num[-3:] + result
    num = num[:-3]
result = num + result

print("Total lines :", result)
print("===== End of progam =====")
