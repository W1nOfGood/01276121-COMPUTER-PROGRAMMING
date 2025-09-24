print(" *** 2 Largest even integers ***")

num_inp = input("Enter a sequence of integers: ").split()
num_list = []
even_num = []

for i in range(len(num_inp)):
    num_list.append(int(num_inp[i]))
    if num_list[i] % 2 == 0:
        even_num.append(num_list[i])
    else:
        continue
even_num.sort()
if len(even_num) > 2:
    print(f"The largest even integer is {even_num[-1]}\nThe second-largest even integer is {even_num[-2]}")
else:
    print("Insufficient input data")
print("===== End of program =====")


# Write a program to accept integer inputs and find the largest and second-largest even numbers. Then, print both values according to the example.

# The input will contain no duplicate values.

# If there are fewer than two even numbers, print the message "Insufficient input data".

# Testcase: 1 / 8 [ 1 to 10 ]
# ✔ Correct
# Expected Output
#  *** 2 Largest even integers ***
# Enter a sequence of integers: 1 2 3 4 5 6 7 8 9 10
# The largest even integer is 10
# The second-largest even integer is 8
# ===== End of program =====
# Student Output
#  *** 2 Largest even integers ***
# Enter a sequence of integers: 1 2 3 4 5 6 7 8 9 10
# The largest even integer is 10
# The second-largest even integer is 8
# ===== End of program =====
# Testcase: 2 / 8 [ Insufficient input data ]
# ✔ Correct
# Expected Output
#  *** 2 Largest even integers ***
# Enter a sequence of integers: 1 2
# Insufficient input data
# ===== End of program =====
# Student Output
#  *** 2 Largest even integers ***
# Enter a sequence of integers: 1 2
# Insufficient input data
# ===== End of program =====
# Testcase: 3 / 8
# ✔ Correct
# Expected Output
#  *** 2 Largest even integers ***
# Enter a sequence of integers: 19 16 14 12 10 11 13 15 17 18
# The largest even integer is 18
# The second-largest even integer is 16
# ===== End of program =====
# Student Output
#  *** 2 Largest even integers ***
# Enter a sequence of integers: 19 16 14 12 10 11 13 15 17 18
# The largest even integer is 18
# The second-largest even integer is 16
# ===== End of program =====
# Testcase: 4 / 8
# ✔ Correct
# Expected Output
#  *** 2 Largest even integers ***
# Enter a sequence of integers: -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
# The largest even integer is -2
# The second-largest even integer is -4
# ===== End of program =====
# Student Output
#  *** 2 Largest even integers ***
# Enter a sequence of integers: -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
# The largest even integer is -2
# The second-largest even integer is -4
# ===== End of program =====
# Testcase: 5 / 8
# ✔ Correct
# Expected Output
#  *** 2 Largest even integers ***
# Enter a sequence of integers: -5 3 -1 5 -3 2 -4 1 -2 4
# The largest even integer is 4
# The second-largest even integer is 2
# ===== End of program =====
# Student Output
#  *** 2 Largest even integers ***
# Enter a sequence of integers: -5 3 -1 5 -3 2 -4 1 -2 4
# The largest even integer is 4
# The second-largest even integer is 2
# ===== End of program =====
# Testcase: 6 / 8
# ✔ Correct
# Expected Output
#  *** 2 Largest even integers ***
# Enter a sequence of integers: 0
# Insufficient input data
# ===== End of program =====
# Student Output
#  *** 2 Largest even integers ***
# Enter a sequence of integers: 0
# Insufficient input data
# ===== End of program =====
# Testcase: 7 / 8
# ✔ Correct
# Expected Output
#  *** 2 Largest even integers ***
# Enter a sequence of integers: 7 8 22 55 169 168
# The largest even integer is 168
# The second-largest even integer is 22
# ===== End of program =====
# Student Output
#  *** 2 Largest even integers ***
# Enter a sequence of integers: 7 8 22 55 169 168
# The largest even integer is 168
# The second-largest even integer is 22
# ===== End of program =====