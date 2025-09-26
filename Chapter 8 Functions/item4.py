print(" *** Triangle Checker ***")
a, b, c = input("Enter side1 side2 side3 : ").split()

def checktri(a,b,c):
    try:
        a = float(a)
        b = float(b)
        c = float(c)
        if a < 0 or b < 0 or c < 0:
            message = "INPUTs cannot be negative."
        elif a == 0 or b == 0 or c == 0:
            message = "Side of triangle must not be zero."
        elif a+b < c or b+c < a or c+a < b:
            message = "==> NOT VALID sides."
        elif a == b == c:
            message = "==> Equilateral Triangle."
        elif a == b or b == c or a == c:
            message = "==> Isosceles Triangle."
        elif int(a)**2 == int(b)+int(c) or int(b)**2 == int(a)+int(c) or int(c)**2 == int(a)+int(b):
            message = "==> Right Triangle."
        else:
            message = "==> Triangle."
        return message
    except:
        message = f"==> Enter 3 numberic number ! ! !"
        return message

message = checktri(a,b,c)
print(message)