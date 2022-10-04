"""
Problema 2
"""

class Persona:
    def __init__(self, edad: int, sexo: str):
        self.edad = edad
        self.sexo = sexo

    def esMasculina(self):
        return self.sexo == 'M'
    

    def esMayor(self):
        return self.edad >= 18

    def __str__(self):
        return '({},{})'.format(self.edad, self.sexo)

    def __repr__(self):
        return self.__str__()


def leer_personas(n = 50):
    personas = []
    mayores, mayores_masc, mayores_fem, masc = 0, 0, 0, 0
    print('Leer personas edad: int, sexo: char M/F')
    for _ in range(n):
        edad, sexo = int(input()), input()
        p = Persona(edad, sexo)
        personas.append(p)
        if p.esMayor():
            mayores += 1
            if p.esMasculina():
                mayores_masc +=1
            else: 
                mayores_fem +=1
        if p.esMasculina():
            masc +=1
    return personas, mayores, mayores_masc, mayores_fem, masc

n_personas = 50
personas, mayores, mayores_masc, mayores_fem, masc = leer_personas(n_personas)
print('Hay {} mayores de edad'.format(mayores))
print('Hay {} menores de edad'.format(n_personas-mayores))
print('Hay {} varones mayores de edad'.format(mayores_masc))
print('Hay {} mujeres menores de edad'.format(n_personas-masc-mayores_fem))
print('Porcentaje de mayores de edad frente a total {}%'.format(mayores*100/n_personas))
print('Porcentaje de mujeres frente a total {}%'.format((n_personas-masc)*100/n_personas))


