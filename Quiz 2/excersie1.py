print(" *** Fibonacci sequence ***")
a0, a1, n = input("Enter a0 a1 n : ").split()

a0, a1, n, fibo_str = int(a0), int(a1), int(n), f'{a0}, {a1}'
i = 0
while i != n-2:
    a0, a1 = a1, a0 + a1
    fibo_str += f', {a1}'
    i += 1
print(fibo_str)
print("===== End of program =====")



# Write a program to take three numbers as input: a0, a1, and n.

# a0 and a1 are integers.

# Each subsequent number will be the sum of the previous two numbers.

# n is the number of terms to display.

# For example, if the input is 3, 5, and 6, the output will be:

# 3, 5, 8, 13, 21, 34

# Use while loop only

# Testcase: 1 / 7
# ✔ Correct
# Expected Output
#  *** Fibonacci sequence ***
# Enter a0 a1 n : 3 5 6
# 3, 5, 8, 13, 21, 34
# ===== End of program =====
# Student Output
#  *** Fibonacci sequence ***
# Enter a0 a1 n : 3 5 6
# 3, 5, 8, 13, 21, 34
# ===== End of program =====
# Testcase: 2 / 7
# ✔ Correct
# Expected Output
#  *** Fibonacci sequence ***
# Enter a0 a1 n : 0 1 5
# 0, 1, 1, 2, 3
# ===== End of program =====
# Student Output
#  *** Fibonacci sequence ***
# Enter a0 a1 n : 0 1 5
# 0, 1, 1, 2, 3
# ===== End of program =====
# Testcase: 3 / 7
# ✔ Correct
# Expected Output
#  *** Fibonacci sequence ***
# Enter a0 a1 n : 1 -1 9
# 1, -1, 0, -1, -1, -2, -3, -5, -8
# ===== End of program =====
# Student Output
#  *** Fibonacci sequence ***
# Enter a0 a1 n : 1 -1 9
# 1, -1, 0, -1, -1, -2, -3, -5, -8
# ===== End of program =====
# Testcase: 4 / 7
# ✔ Correct
# Expected Output
#  *** Fibonacci sequence ***
# Enter a0 a1 n : -1 1 9
# -1, 1, 0, 1, 1, 2, 3, 5, 8
# ===== End of program =====
# Student Output
#  *** Fibonacci sequence ***
# Enter a0 a1 n : -1 1 9
# -1, 1, 0, 1, 1, 2, 3, 5, 8
# ===== End of program =====
# Testcase: 5 / 7
# ✔ Correct
# Expected Output
#  *** Fibonacci sequence ***
# Enter a0 a1 n : 1 2 13
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377
# ===== End of program =====
# Student Output
#  *** Fibonacci sequence ***
# Enter a0 a1 n : 1 2 13
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377
# ===== End of program =====
# Testcase: 6 / 7
# ✔ Correct
# Expected Output
#  *** Fibonacci sequence ***
# Enter a0 a1 n : 0 1 13
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
# ===== End of program =====
# Student Output
#  *** Fibonacci sequence ***
# Enter a0 a1 n : 0 1 13
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
# ===== End of program =====
# Testcase: 7 / 7 [Hidden]
# ✔ Correct
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
