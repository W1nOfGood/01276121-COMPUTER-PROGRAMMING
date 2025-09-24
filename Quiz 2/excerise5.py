print(" *** Rectangle Spiral Fill ***")
width, height = input("Enter width height : ").split()
width = int(width)
height = int(height)

matrix = [[0] * width for _ in range(height)]

row = 0
col = 0
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # R, D, L, U
current_direction = 0

for num in range(1, width * height + 1):
    matrix[row][col] = num

    if num == width * height:
        break

    next_row = row + directions[current_direction][0]
    next_col = col + directions[current_direction][1]

    is_out_of_bounds = not (0 <= next_row and next_row < height and 0 <= next_col and next_col < width)
    is_filled = False
    if not is_out_of_bounds:
        if not (matrix[next_row][next_col] == 0):
            is_filled = True
    
    if is_out_of_bounds or is_filled:
        current_direction = (current_direction + 1) % 4

    row = row + directions[current_direction][0]
    col = col + directions[current_direction][1]


max_num = width * height
padding = len(str(max_num))

for row_list in matrix:
    for num in row_list:
        num_as_str = str(num)
        
        if max_num > 9:
            num_len = len(num_as_str)
            zeros_needed = padding - num_len
            for _ in range(zeros_needed):
                print("0", end="")
        
        print(num_as_str, end=" ")
    print()

print("===== End of program =====")








# Write a Python program that accepts two integers: width and height of a rectangle.

# The program should fill the rectangle with numbers starting from 1 up to width × height.

# The filling pattern must follow a spiral order, starting from the top-left corner, then moving:

# Right → across the top row

# Down ↓ the rightmost column

# Left ← across the bottom row

# Up ↑ the leftmost column

# Repeat this process until the rectangle is completely filled.

# Finally, print the rectangle so that numbers are properly aligned.



# You may use the following program as a guidance



# print(" *** Rectangle Spiral Fill ***")

# width, height = input("Enter width height : ").split()
# width, height = int(width), int(height)

# # create empty matrix with zero fill
# matrix = [[0] * width for _ in range(height)]

# n = 1
# for row in range(height):
#     for col in range(width):
#         matrix[row][col] = n 
#         n += 1

# # display result
# max_width = len(str(width * height))  
# # print(f"max_width={max_width}")
# for row in matrix:
#     for num in row:
#         print(f"{num:{0}{max_width}d}", end=" ")
#     print()
# print("===== End of program =====")


# Result:

#  *** Rectangle Spiral Fill ***
# Enter width height : 6 4
# 01 02 03 04 05 06 
# 07 08 09 10 11 12
# 13 14 15 16 17 18
# 19 20 21 22 23 24
# ===== End of program =====



# x



# Testcase: 1 / 10
# Expected Output
#  *** Rectangle Spiral Fill ***
# Enter width height : 4 5
# 01 02 03 04 
# 14 15 16 05 
# 13 20 17 06 
# 12 19 18 07 
# 11 10 09 08 
# ===== End of program =====
# Student Output
# Waiting for submission . . .
# Testcase: 2 / 10
# Expected Output
#  *** Rectangle Spiral Fill ***
# Enter width height : 1 2
# 1 
# 2 
# ===== End of program =====
# Student Output
# Waiting for submission . . .
# Testcase: 3 / 10
# Expected Output
#  *** Rectangle Spiral Fill ***
# Enter width height : 6 6
# 01 02 03 04 05 06 
# 20 21 22 23 24 07 
# 19 32 33 34 25 08 
# 18 31 36 35 26 09 
# 17 30 29 28 27 10 
# 16 15 14 13 12 11 
# ===== End of program =====
# Student Output
# Waiting for submission . . .
# Testcase: 4 / 10
# Expected Output
#  *** Rectangle Spiral Fill ***
# Enter width height : 6 7
# 01 02 03 04 05 06 
# 22 23 24 25 26 07 
# 21 36 37 38 27 08 
# 20 35 42 39 28 09 
# 19 34 41 40 29 10 
# 18 33 32 31 30 11 
# 17 16 15 14 13 12 
# ===== End of program =====
# Student Output
# Waiting for submission . . .
# Testcase: 5 / 10
# Expected Output
#  *** Rectangle Spiral Fill ***
# Enter width height : 4 1
# 1 2 3 4 
# ===== End of program =====
# Student Output
# Waiting for submission . . .
# Testcase: 6 / 10
# Expected Output
#  *** Rectangle Spiral Fill ***
# Enter width height : 3 2
# 1 2 3 
# 6 5 4 
# ===== End of program =====
# Student Output
# Waiting for submission . . .
# Testcase: 7 / 10
# Expected Output
#  *** Rectangle Spiral Fill ***
# Enter width height : 10 10
# 001 002 003 004 005 006 007 008 009 010 
# 036 037 038 039 040 041 042 043 044 011 
# 035 064 065 066 067 068 069 070 045 012 
# 034 063 084 085 086 087 088 071 046 013 
# 033 062 083 096 097 098 089 072 047 014 
# 032 061 082 095 100 099 090 073 048 015 
# 031 060 081 094 093 092 091 074 049 016 
# 030 059 080 079 078 077 076 075 050 017 
# 029 058 057 056 055 054 053 052 051 018 
# 028 027 026 025 024 023 022 021 020 019 
# ===== End of program =====
# Student Output
# Waiting for submission . . .
# Testcase: 8 / 10 [Hidden]
# Testcase: 9 / 10 [Hidden]
# Testcase: 10 / 10
# Expected Output
#  *** Rectangle Spiral Fill ***
# Enter width height : 4 8
# 01 02 03 04 
# 20 21 22 05 
# 19 32 23 06 
# 18 31 24 07 
# 17 30 25 08 
# 16 29 26 09 
# 15 28 27 10 
# 14 13 12 11 
# ===== End of program =====
# Student Output
# Waiting for submission . . .

# ⚙️ Chapter Restrictions (Quiz #2 ch 1-6
# Sep 12, 2025
# )
# Reserved Words:
# ✅ False, None, True, and, break, continue, elif, else, except, finally, for, if, in, is, not, or, try, while
# ❌ as, assert, async, await, case, class, def, del, from, global, import, lambda, match, nonlocal, pass, raise, return, with, yield
# Built-in Functions:
# ✅ bool, chr, enumerate, float, id, input, int, len, list, max, min, ord, print, range, str, sum, type
# ❌ __import__, abs, aiter, all, anext, any, ascii, bin, breakpoint, bytearray, bytes, callable, classmethod, compile, complex, delattr, dict, dir, divmod, eval, exec, filter, format, frozenset, getattr, globals, hasattr, hash, help, hex, isinstance, issubclass, iter, locals, map, memoryview, next, object, oct, open, pow, property, repr, reversed, round, set, setattr, slice, sorted, staticmethod, super, tuple, vars, zip
# Operators:
# ✅ !=, %, %=, *, **, *=, +, +=, -, -=, /, //, /=, <, <=, =, ==, >, >=, and, in, is, not, or
# ❌
# String Methods:
# ✅ encode, lstrip, rstrip, split
# ❌ capitalize, casefold, center, count, endswith, find, format, index, isalnum, isalpha, isdigit, islower, isspace, istitle, isupper, join, lower, replace, rfind, rindex, startswith, strip, swapcase, title, upper, zfill
