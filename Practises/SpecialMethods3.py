# Dada la clase Libro, implementa el método especial __del__ para que el usuario sea informado con el mensaje "Libro eliminado",
# mostrándolo en pantalla cada vez que el libro se elimine.

class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __del__(self):
        print(f'Libro eliminado')

mi_libro = Libro("Luna de Pluton","Paco",35)
del(mi_libro)
