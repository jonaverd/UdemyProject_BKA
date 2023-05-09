import time
import random
import os


class Tools:
    @staticmethod
    def validate_string(input):
        """valida que la entrada contenga solo letras"""
        input = input.replace(" ", "")
        if input.isalpha():
            return True
        else:
            return False

    @staticmethod
    def validate_number(input):
        """valida que la entrada contenga solo numeros"""
        input = input.replace('.', '', 1)
        if input.isdigit():
            return True
        else:
            return False

    @staticmethod
    def clean():
        """limpia el terminal de salida"""
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def aux_printing_bars(percent):
        """dibuja una barra de carga"""
        if percent in range(0, 10):
            print(f"|==                    | {percent}%")
        elif percent in range(10, 20):
            print(f"|====                  | {percent}%")
        elif percent in range(20, 30):
            print(f"|======                | {percent}%")
        elif percent in range(30, 40):
            print(f"|========              | {percent}%")
        elif percent in range(40, 50):
            print(f"|==========            | {percent}%")
        elif percent in range(50, 60):
            print(f"|============          | {percent}%")
        elif percent in range(60, 70):
            print(f"|==============        | {percent}%")
        elif percent in range(70, 80):
            print(f"|================      | {percent}%")
        elif percent in range(80, 90):
            print(f"|==================    | {percent}%")
        elif percent in range(90, 100):
            print(f"|====================  | {percent}%")
        else:
            print(f"|======================| 100%")

    @staticmethod
    def loading_pattern(details="Don't press any key!", preview="Loading operation...", finish="Operation is completed"):
        """simulacion de carga para una operacion"""
        Tools.clean()
        for value in range(0, 110, 10):
            Tools.clean()
            if value >= 100:
                print(finish)
                details = None
            else:
                print(preview)
            Tools.aux_printing_bars(random.randint(value, value + 9))
            if details is not None:
                print(f"\n{details}")
            time.sleep(random.uniform(0.0, random.uniform(1.6, 2.8)))

