#Pruebas unitarias con doctest
def es_divisible_entre_2_o_5(n):
    """
      >>> es_divisible_entre_2_o_5(8)
      True
      >>> es_divisible_entre_2_o_5(7)
      False
      >>> es_divisible_entre_2_o_5(5)
      True
      >>> es_divisible_entre_2_o_5(9)
      False
    """
    return n % 2 == 0 or n % 5 == 0

if __name__ == '__main__':
    import doctest
    doctest.testmod()

#funcion productiva (funciones que devuelven valores) y valor de retorno
#variable temporal
def area(radio):
    temporal = 3.14159 * radio**2
    return temporal

#codigo muerto
def valor_absoluto(x):
    if x < 0:
        return -x
    elif x > 0:
        return x

print valor_absoluto(0)
