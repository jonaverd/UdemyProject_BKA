class Vehiculo:
    def acelerar(self):
        print("Acelero")

    def frenar(self):
        print("Freno")


class Automovil(Vehiculo):
    pass


camion = Automovil()
camion.acelerar()
