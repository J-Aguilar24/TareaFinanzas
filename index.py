class Ingreso:
    saldo = 0
    def __init__(self, ingreso):
        self.ingreso = ingreso

    def aumento(self):
        saldo += self.ingreso
        return saldo

class Egreso:
    def __init__(self, egreso):
        self.egreso = egreso

class Finanzas(Ingreso):
    pass
