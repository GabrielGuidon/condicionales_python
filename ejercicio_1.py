# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de práctica numérica

# Comparadores
# Ingrese dos números cualesquiera y realice las sigueintes
# comparaciones entre ellos
numero_1 = int(input('Ingrese el primer número:\n'))

numero_2 = int(input('Ingrese el segundo número:\n'))

# Compare cual de los dos números es mayor
# Imprima en pantalla según corresponda
if (numero_1 > numero_2): 
    print ('El primer numero ' , numero_1, ' es mayor que el segundo numero', numero_2)
else:
    print ('El segundo numero ' , numero_2, ' es mayor que el primer numero', numero_1)

# Verifique si el numero_1 positivo, negativo o cero
# Imprima el resultado en cada caso
if ( numero_1 > 0):
    print('El primer numero es positivo', numero_1)
elif ( numero_1 < 0):
    print('El primer nunmero es negativo', numero_1)
else: 
    if (numero_1 == 0) and (numero_1 == numero_2):
        print('El primer y el segundo numero es igual a CERO')
    else:
        print ('El primer numero es igual a CERO ',numero_1)

# Verifique si el numero_1 es mayor a 0 y menor a 100
# Imprima en pantalla si se cumple o no la condición
if ( numero_1 > 0):
    print('El primer numero es positivo ', numero_1,)
elif (numero_1 < 100):
    print('EL primer numero es menor a 100 ', numero_1)
elif ( numero_1 == numero_2 == 0) :
    print('Ambos numeros ingresados son igual a cero')

# Verifique si el numero_1 es menor a 10 o el numero_2
# es mayor a -2
# Imprima en pantalla si se cumple o no la condición
if (numero_1 < 10):
    print('Él primer numero es menor a 10', numero_1)
elif (numero_2 > -2):
    print('el segundo numero es mayor a -2 ', numero_2)
