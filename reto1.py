"""
Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
"""

##############################################################################################################################################

#Se declara la variable.
num1 = 10

#Repite el bloque mientras la condición sea verdadera.
while num1 <= 55:
    if num1 % 2 == 0 and num1 != 16 and num1 % 3 != 0 or num1 == 55:
        print(num1)
    num1 += 1