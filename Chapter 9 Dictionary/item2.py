print(" *** Creating Dictionary ***")
usrinp = input("Enter text : ").split()

uhmdic = {}

for i in range(0, len(usrinp), 2):
    key = usrinp[i]
    value = int(usrinp[i + 1])
    
    if key in uhmdic:
        uhmdic[key] += value
    else:
        uhmdic[key] = value

print(uhmdic)
print("===== End of program =====")
