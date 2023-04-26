import os
from random import randint


class Persona:
    """clase para almacenar datos personales"""

    @staticmethod
    def validar_palabra(input):
        """valida que la entrada contenga solo letras"""
        input = input.replace(" ", "")
        if input.isalpha():
            return True
        else:
            return False

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):
    """clase para almacenar datos bancarios"""
    numero_cuenta = None
    balance = None

    @staticmethod
    def validar_numero(input):
        """valida que la entrada contenga solo numeros"""
        input = input.replace('.','',1)
        if input.isdigit():
            return True
        else:
            return False

    @classmethod
    def generar_cuenta(cls, n):
        range_start = 10 ** (n - 1)
        range_end = (10 ** n) - 1
        cls.numero_cuenta = randint(range_start, range_end)
        cls.balance = 0

    def comprobar_saldo(self, cantidad):
        if self.balance == 0:
            limpiar()
            print(f"No hay saldo en la cuenta disponible")
            return False
        elif self.balance - cantidad < 0:
            limpiar()
            print(f"No se puede retirar más de {round(self.balance, 2)}€")
            return False
        else:
            return True

    def depositar(self, cantidad):
        self.balance += cantidad
        limpiar()
        print(f"Operación completada")

    def retirar(self, cantidad):
        if self.comprobar_saldo(cantidad):
            self.balance -= cantidad
            limpiar()
            print(f"Operación completada")

    def __str__(self):
        return f'Cliente {self.nombre.upper()} {self.apellido.upper()} Cuenta {self.numero_cuenta}\n' \
               f'El saldo actual es {round(self.balance, 2)}€'


def limpiar():
    """limpia el terminal de salida"""
    os.system('cls' if os.name == 'nt' else 'clear')


def crear_cliente():
    """crea un cliente a partir de los datos ingresados"""
    print("NUEVO CLIENTE BANKINTER")
    nombre = input("Introduce tu nombre: ")

    while not Persona.validar_palabra(nombre):
        limpiar()
        print("NUEVO CLIENTE BANKINTER")
        nombre = input("Introduce tu nombre: ")
    else:
        limpiar()
        print("NUEVO CLIENTE BANKINTER")
        apellido = input("Introduce tu apellido: ")

        while not Persona.validar_palabra(apellido):
            limpiar()
            print("NUEVO CLIENTE BANKINTER")
            apellido = input("Introduce tu apellido: ")
        else:
            cliente = Cliente(nombre, apellido)
            cliente.generar_cuenta(10)
            return cliente


def operaciones():
    """opciones disponibles del menu"""
    print(f"\n[1] Depositar dinero\n"
          f"[2] Retirar dinero\n"
          f"[3] Salir\n")


def menu(cliente):
    """bucle para seleccionar operaciones bancarias"""
    print("BANKINTER")
    print(cliente)
    operaciones()

    option = input("¿Que desea hacer? ")

    while not option == '3':
        if option == '1':
            limpiar()
            print("BANKINTER (DEPOSITAR)")
            print(f">> Cuenta seleccionada {cliente.numero_cuenta}")
            cantidad = input("\nIndique la cantidad a ingresar: ")

            while not Cliente.validar_numero(cantidad):
                limpiar()
                print("BANKINTER (DEPOSITAR)")
                print(f">> Cuenta seleccionada {cliente.numero_cuenta}")
                cantidad = input("\nIndique la cantidad a ingresar: ")

            else:
                cliente.depositar(float(cantidad))
                input("\n<< pulsa para volver >> ")

        elif option == '2':
            limpiar()
            print("BANKINTER (RETIRAR)")
            print(f">> Cuenta seleccionada {cliente.numero_cuenta}")
            cantidad = input("\nIndique la cantidad a extraer: ")

            while not Cliente.validar_numero(cantidad):
                limpiar()
                print("BANKINTER (RETIRAR)")
                print(f">> Cuenta seleccionada {cliente.numero_cuenta}")
                cantidad = input("\nIndique la cantidad a extraer: ")

            else:
                cliente.retirar(float(cantidad))
                input("\n<< pulsa para volver >> ")

        limpiar()
        print("BANKINTER")
        print(cliente)
        operaciones()

        option = input("¿Que desea hacer? ")

    else:
        limpiar()
        print("BANKINTER (SALIR)")
        print(f"¡Hasta pronto!")


def inicio():
    """ejecuta el programa principal"""
    limpiar()
    cliente = crear_cliente()
    limpiar()
    menu(cliente)


inicio()
