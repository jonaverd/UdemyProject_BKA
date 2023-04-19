# Crea una clase llamada Mascota, que tenga los siguientes atributos de instancia: edad, nombre, cantidad_patas.
# Crea otra clase, Perro, que herede de la primera sus atributos.

class Mascota:
    def __init__(self, edad, nombre, cantidad_patas):
        self.edad = edad
        self.nombre = nombre
        self.cantidad_patas = cantidad_patas


class Perro(Mascota):
    pass


perro = Perro(5, "Crash", 4)
print(perro.cantidad_patas)