print(" *** String Rotation ***")
raw = input("Enter string / step : ")

p = raw.find('/')
left = raw[:p].strip()
right = raw[p+1:].strip()

s = left
n = len(s)
step = int(right)

if n == 0:
    rot_times = 0
    smod = 0
else:
    smod = step % n
    if smod == 0:
        rot_times = 1
    else:
        a = n
        b = smod
        while b != 0:
            t = a % b
            a = b
            b = t
        g = a
        rot_times = n // g

print("The rotation times = " + str(rot_times))

pad2 = 0
if rot_times >= 10:
    pad2 = 1

if rot_times <= 20:
    cur = s
    if pad2 == 1 and 0 < 10:
        idx = "0" + str(0)
    else:
        idx = str(0)
    print(idx + " ==> " + cur)

    i = 1
    while i <= rot_times:
        if n > 0:
            cur = cur[smod:] + cur[:smod]
        if pad2 == 1 and i < 10:
            idx = "0" + str(i)
        else:
            idx = str(i)
        print(idx + " ==> " + cur)
        i += 1
else:
    cur = s
    i = 0
    while i <= 4:
        if pad2 == 1 and i < 10:
            idx = "0" + str(i)
        else:
            idx = str(i)
        print(idx + " ==> " + cur)
        i += 1
        if i <= 4 and n > 0:
            cur = cur[smod:] + cur[:smod]

    print(" . . . . .")

    if n == 0:
        cur = s
    else:
        k = rot_times - 4
        q = k // n
        k_mod_n = k - q * n
        total_shift = (k_mod_n * smod) % n
        cur = s[total_shift:] + s[:total_shift]

    j = rot_times - 4
    while j <= rot_times:
        if pad2 == 1 and j < 10:
            idx = "0" + str(j)
        else:
            idx = str(j)
        print(idx + " ==> " + cur)
        j += 1
        if j <= rot_times and n > 0:
            cur = cur[smod:] + cur[:smod]

print("===== End of program =====")