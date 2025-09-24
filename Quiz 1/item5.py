print(" *** Triangle Checker ***")
a, b, c = input("Enter triangle sides : ").split()

try:
    a = int(a)
    b = int(b)
    c = int(c)
    if a + b <= c or b + c <= a or c + a <= b:
        print("That's not triangle")
    elif a == b == c:
        print("That's a equilateral triangle")
    elif a == b or b == c or a == c:
        print("That's isosceles triangle")
    elif a**2 == b+c or b**2 == a+c or c**2 == a+b:
        print("That's a Right triangle")
    else:
        print("That's a simple triangle")
except:
    print("Enter 3 numberic number ! ! !")
    
print("===== End of program =====")