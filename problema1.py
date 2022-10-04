"""
Problema 1
"""

numero = int(input('Leer numero\n'))
if numero % 2 == 0:
    print('El numero {} es par'.format(numero))
else:
    print('El numero {} es impar'.format(numero))

# Para ambos casos debemos restar 2
while numero >= 0:
    print(numero, end=' ')
    numero = numero - 2
