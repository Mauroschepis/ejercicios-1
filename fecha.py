a=int(input("ingresar año: "))
m=int(input("ingresar mes: "))
d=int(input("ingresar dia: "))

print("Ingresar una fecha")

if d>0 and d<30:
    print(d+1)
    print(m)
    print(a)
else:
    if m>0 and m<12:
        print("1")
        print(m+1)
        print(a)
    else:
        print("1")
        print("1")
        print(a+1)



