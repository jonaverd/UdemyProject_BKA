# La función incorporada en Python len() tiene un comportamiento polimórfico, ya que calcula el largo de un objeto
# en función de su tipo (strings, listas, tuples, entre otros),
# devolviendo la cantidad de items o caracteres que lo componen.
# Crea un iterador que recorra los siguientes objetos: palabra, lista, tupla y muestre en pantalla (print()) para cada uno de
# ellos su longitud con la función len().
# Puedes recordar cómo implementar la función len() siguiente enlace: https://docs.aws.amazon.com/es_es/redshift/latest/dg/r_LEN.html

palabra = "polimorfismo"
lista = ["Clases", "POO", "Polimorfismo"]
tupla = (1, 2, 3, 80)


def iterador(objeto):
    print(len(objeto))

iterador(palabra)
iterador(lista)
iterador(tupla)