A=float(input("Ingresar valor cuadratico A: "))
B=float(input("Ingresar valor cuadratico B: "))
C=float(input("Ingresar valor cuadratico C: "))
D=float

D=B**2-4*A*C

if D>0:
    x1=((-B)+D**0.5)/2*A
    x2=((-B)-D**0.5)/2*A
    print("Raices reales", x1, x2)
else:
    print("Raices irracionales")

