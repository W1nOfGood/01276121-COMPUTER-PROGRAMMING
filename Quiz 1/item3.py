print(" *** Smart Calculator ***")
a, b = input("Enter any 2 type : ").split()
try:
    a = float(a)
    b = float(b)
    try:
        total = float(a*b)
        if int(total) == total :
            print(f"output ==> {int(total)}")
        else:
            print(f"output ==> {total}")
    except:
        total = a*b
        print(f"output ==> {total}")
        
except:
    try:
        b = float(b)
        try:
            a = int(a)
            final = a*b
            print(f"output ==> {final}")
        except:
            b = int(b)
            final = a*b
            print(f"output ==> {final}")
        
    except:
        if int(a) == a :
            a = int(a)
            final = a*b
            print(f"output ==> {final}")
        else:
            print(f"output ==> {a}{b}")
            

print("===== End of program =====")