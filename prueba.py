from index import *

while True:

    finanzasObj = Finanzas()

    print("Menu: \n")
    print("(0) salir")
    print("(1) Realizar Ingreso")
    print("(2) Realizar Egreso")
    print("(3) Reporte de ingreso")
    print("(4) Reporte de egreso")
    print("(5) Reporte de transacciones")
    print("(6) Total")
    tipo = int(input(" Escoge una opcion: "))
    if tipo==0:
        break
    elif tipo==1:
        # Class ingreso
        ingreso = float(input("Cuanto deseas ingresar?\n"))
        finanzasObj.aumento(ingreso)
        print(ingreso)

    elif tipo==2:
        egresos = float(input("Cuanto deseas extraer? "))
        finanzasObj.reduccion(egresos)

    elif tipo==3:
        pass

    elif tipo==4:
        pass

    elif tipo==5:
        transacciones = finanzasObj.transacciones()
        
    elif tipo==6:
        print(saldo)
