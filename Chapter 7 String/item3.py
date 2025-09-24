print(" *** Kebab string ***")
x = input("Enter some words: ").split()
wordslower = []
for i in x:
    wordslower.append(i.lower())

strings = "-".join(wordslower)
print("Kebab-case => " + strings)
print("===== End of program ======")