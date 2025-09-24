print(" *** Sum of serie ***")
r, N = input("Enter r N : ").split()

try:
    r, N, str_numpls, total = int(r), int(N), '', 0
    for i in range(N):
        numpls = r**i
        if str_numpls:
            str_numpls += f'+'
        str_numpls += f"{numpls}"
        total += numpls
    print(f"{str_numpls} = {total}")
except:
    print("Input must be an integer !!!")

print("===== End of program =====")




# Testcase: 1 / 11
# ✔ Correct
# Expected Output
#  *** Sum of serie ***
# Enter r N : 3 5
# 1+3+9+27+81 = 121
# ===== End of program =====
# Student Output
#  *** Sum of serie ***
# Enter r N : 3 5
# 1+3+9+27+81 = 121
# ===== End of program =====
# Testcase: 2 / 11 [Hidden]
# ✔ Correct
# Testcase: 3 / 11 [Hidden]
# ✔ Correct
# Testcase: 4 / 11
# ✔ Correct
# Expected Output
#  *** Sum of serie ***
# Enter r N : 3.5 10
# Input must be an integer !!!
# ===== End of program =====
# Student Output
#  *** Sum of serie ***
# Enter r N : 3.5 10
# Input must be an integer !!!
# ===== End of program =====
# Testcase: 5 / 11 [Hidden]
# ✔ Correct
# Testcase: 6 / 11
# ✔ Correct
# Expected Output
#  *** Sum of serie ***
# Enter r N : 3 10.0
# Input must be an integer !!!
# ===== End of program =====
# Student Output
#  *** Sum of serie ***
# Enter r N : 3 10.0
# Input must be an integer !!!
# ===== End of program =====
# Testcase: 7 / 11 [Hidden]
# ✔ Correct
# Testcase: 8 / 11
# ✔ Correct
# Expected Output
#  *** Sum of serie ***
# Enter r N : hi 30
# Input must be an integer !!!
# ===== End of program =====
# Student Output
#  *** Sum of serie ***
# Enter r N : hi 30
# Input must be an integer !!!
# ===== End of program =====
# Testcase: 9 / 11 [Hidden]
# ✔ Correct
# Testcase: 10 / 11
# ✔ Correct
# Expected Output
#  *** Sum of serie ***
# Enter r N : -1 5
# 1+-1+1+-1+1 = 1
# ===== End of program =====
# Student Output
#  *** Sum of serie ***
# Enter r N : -1 5
# 1+-1+1+-1+1 = 1
# ===== End of program =====
# Testcase: 11 / 11
# ✔ Correct
# Expected Output
#  *** Sum of serie ***
# Enter r N : 3 7
# 1+3+9+27+81+243+729 = 1093
# ===== End of program =====
# Student Output
#  *** Sum of serie ***
# Enter r N : 3 7
# 1+3+9+27+81+243+729 = 1093
# ===== End of program =====
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