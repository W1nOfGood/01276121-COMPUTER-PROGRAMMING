usrinp = input("Enter : ")

words = usrinp.split()

word_counts = {}
total_count = {}

for word in words:
    word_count = {}
    for char in word:
        if char in word_count:
            word_count[char] += 1
        else:
            word_count[char] = 1
        
        if char in total_count:
            total_count[char] += 1
        else:
            total_count[char] = 1
    
    word_counts[word] = word_count

for word, count in word_counts.items():
    print(f"{word} = {count}")

max_char = max(total_count, key=total_count.get)
max_count = total_count[max_char]

if len(words) > 1:
    print(f"{usrinp} = {total_count}")
print(f"Maximum Character Count: {max_char} {max_count}")
print("===== End of program =====")
