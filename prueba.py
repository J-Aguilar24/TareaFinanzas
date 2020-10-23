from index import *

while True:

    saldo = 0.00
    ingresoObj = Ingreso()
    egresoObj = Egreso()
    finanzasObj = Finanzas()

    print("Bienvenido al proyecto de Finanzas Personales\n")
    tipo = int(input("Presione 0 si desea salir, 1 si desea realizar un ingreso o 2 si desea hacer un egreso\n"))
    if tipo==0:
        break
    elif tipo==1:
        # Class ingreso
        ingreso = float(input("Cuanto deseas ingresar?\n"))
        cantidad = finanzasObj.aumento(50)
        print(cantidad)
    else:
        #Class Egreso
       pass

