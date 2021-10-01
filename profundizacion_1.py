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
Realice un programa que solicite por consola 2 números
Calcule la diferencia entre ellos e informe por pantalla
si el resultado es positivo, negativo o cero.
'''
print('Ingrese primer numero: ')
numero_1 = int(input())
print('Ingrese primer numero: ')
numero_2 = int(input())
resultado = numero_1 - numero_2
if (numero_1 > numero_2):
    print ('el primer numero ', numero_1, 'es mayor que el segundo numero ',numero_2, 'su diferencia es ', resultado)
else:
    if (numero_1 < numero_2):
         print ('el primer numero ', numero_1, 'es menor que el segundo numero ',numero_2, 'su diferencia es ', resultado)
    else:
         print ('el primer numero ', numero_1, 'y el segundo numero ',numero_2, ' son iguales y su diferencia es CERO')
       
# Empezar aquí la resolución del ejercicio