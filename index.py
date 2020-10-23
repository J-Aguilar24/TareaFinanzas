saldo = 0
class Ingreso:
    def __init__(self):
        self.ingreso = 0

    def aumento(self, ingreso):
        self.ingreso += saldo

    def showIngresos(self):
        return self.ingreso

class Egreso:
    def __init__(self, egreso):
        self.egreso = egreso
        self.listEgreso = []

    def reduccion(self, egresos):
        self.egreso += saldo


class Finanzas(Ingreso, Egreso):
    def getSaldo(self):
        return saldo

    def transacciones(self):
        return Egreso.reduccion, Ingreso.aumento 
