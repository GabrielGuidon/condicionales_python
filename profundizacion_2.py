# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un programa que solicite el ingreso de tres números
enteros, y luego en cada caso informe si el número es par
o impar.
Para cada caso imprimir el resultado en pantalla.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio
print('Ingrese primer numero: ')
numero_1 = int(input())
print('Ingrese primer numero: ')
numero_2 = int(input())
print('Ingrese primer numero: ')
numero_3 = int(input())
if numero_1 % 2 == 0:
    print('El número', numero_1, 'es par.')
else:
    print('El número', numero_1, 'es impar.')
if numero_2 % 2 == 0:
    print('El número', numero_2, 'es par.')
else:
    print('El número', numero_2, 'es impar.')
if numero_3 % 2 == 0:
    print('El número', numero_3, 'es par.')
else:
    print('El número', numero_3, 'es impar.')
if(numero_1 == numero_2 == numero_3):
    print('Los 3 numeros son iguales')