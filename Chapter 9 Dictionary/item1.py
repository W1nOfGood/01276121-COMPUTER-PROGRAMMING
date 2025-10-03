print(" *** Creating Dictionary ***")
usrinp = input("Enter text : ").split()

dex, secdex, uhmdic, count = 0, 1, {}, 0

for i in usrinp:
    if count < len(usrinp)//2:
        count += 1
        uhmdic[usrinp[dex]] = usrinp[secdex]
        dex += 2
        secdex += 2
    else:
        break

print(uhmdic)
print("===== End of program =====")