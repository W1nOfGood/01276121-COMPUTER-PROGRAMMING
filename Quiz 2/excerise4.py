print(" *** Pyramid / Cone display ***")
n = int(input('Enter height : '))

pattern = []
total = 0
for i in range(1, n + 1):
    row = []
    
    # Uhm the left up bruh
    for j in range(n - i):
        row = row + [' ']
    for k in range(2 * i - 1):
        row = row + ['*']
        total = total + 1
    for j in range(n - i):
        row = row + [' ']
            
            # middele ||||
    row = row + [' ', '|', ' ']
    
    # right dsown
    for j in range(i - 1):
        row = row + [' ']
    for j in range(2 * (n - i) + 1):
        row = row + ['*']
        total = total + 1
    for j in range(i - 1):
        row = row + [' ']
            
    pattern = pattern + [row]

for row_list in pattern:
    for char in row_list:
        print(char, end='')
    print()
print("Total(*) = ", total)







# Musashi has developed a program that operates as shown in the diagram.

#  ***  Cone display ***
# Enter height : 5
# *********
#  *******
#   *****
#    ***
#     *
# Total(*) = 25


#The source code obtained is

# print(" ***  Cone display ***")
# str = input("Enter height : ")
# num = int(str)
# if num<3:
#     print(f'The input "{num}" must greater than 2 !!!')
#     quit()
# count=0
# ch = '*'
# for r in range(num):
    
#     for c in range(2*num-1):
#         if c>=r :
#             if r+c < 2*num-1:
#                 print(ch,end='')
#                 count +=1
#             else:
#                 print(" ",end='')
#         else:
#             print(" ",end='')
#     print()
# print(f"Total({ch}) = {count}")


# Jennifer came across it and wants to further develop it into

#  *** Pyramid / Cone display ***
# Enter height : 5
#     *     | *********
#    ***    |  *******
#   *****   |   *****
#  *******  |    ***
# ********* |     *
# Total(*) = 50


# Your task is to help Jennifer complete the development.

# Testcase: 1 / 6
# Expected Output
#  *** Pyramid / Cone display ***
# Enter height : 5
#     *     | *********
#    ***    |  ******* 
#   *****   |   *****  
#  *******  |    ***   
# ********* |     *    
# Total(*) = 50
# Student Output
# Waiting for submission . . .
# Testcase: 2 / 6 [ จำนวนน้อยกว่า 3 ]
# Expected Output
#  *** Pyramid / Cone display ***
# Enter height : 0
# The input "0" must greater than 2 !!!
# Student Output
# Waiting for submission . . .
# Testcase: 3 / 6 [ จำนวนน้อยกว่า 3 ] [Hidden]
# Testcase: 4 / 6 [ จำนวนสองหลัก ] [Hidden]
# Testcase: 5 / 6 [ จำนวนสองหลัก ] [Hidden]
# Testcase: 6 / 6
# Expected Output
#  *** Pyramid / Cone display ***
# Enter height : 9
#         *         | *****************
#        ***        |  *************** 
#       *****       |   *************  
#      *******      |    ***********   
#     *********     |     *********    
#    ***********    |      *******     
#   *************   |       *****      
#  ***************  |        ***       
# ***************** |         *        
# Total(*) = 162
# Student Output
# Waiting for submission . . .
# No file chosen
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

