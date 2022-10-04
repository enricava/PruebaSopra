"""
Problema 3
"""

horastrabajadas = float(input('Leer horas trabajadas\n'))
tarifa = float(input('Leer tarifa\n'))
cantidad_max = 40

sueldo = 0
horasextra = horastrabajadas - cantidad_max
sueldo += (horastrabajadas - horasextra) * tarifa
if horasextra > 0:
    sueldo += horasextra * tarifa * 1.5
print(sueldo)