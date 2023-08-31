Audi=float(input("ingresar la velocidad del Audi R8: "))
Pagani=float(input("ingresar la velocidad del Pagani Zonda R: "))
dist=float(input("ingresar distancia que los separa a los vehiculos: "))
t=float

if Audi>0 and Pagani>0:
 t=dist/(Audi+Pagani)
 print(t)
else:
 print("Error")
