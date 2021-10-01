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
Realice un programa que solicite ingresar tres valores de temperatura
De las temperaturas ingresadas por consola determinar:
1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
3 - ¿Cuál es el promedio de las temperaturas ingresadas?

En cada caso imprimir en pantalla el resultado

IMPORTANTE: Para ordenar las temperatuas debe utilizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido. Recomendamos pensar bien este problema de lógica con un lápiz y papel.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio
print('Ingrese primer valor: ')
temperatura_1 = int(input())
print('Ingrese segundo valor: ')
temperatura_2 = int(input())
print('Ingrese tercer valor: ')
temperatura_3 = int(input())

max = int()
max = 0
if ((temperatura_1 ) > (temperatura_2)):
    if ((temperatura_2) > temperatura_3) :
        if (temperatura_3 > temperatura_1):
                max = temperatura_3
                min = temperatura_2
        else:
                max = temperatura_1
                min = temperatura_3
    else:
        if(temperatura_3 >temperatura_1):
            max = temperatura_3
            min = temperatura_2
        else:
            max = temperatura_3
            min = temperatura_2
else:
    if(temperatura_2 > temperatura_3):
        if(temperatura_3 > temperatura_1):
            max = temperatura_2
            min = temperatura_1
        else:
            max = temperatura_2
            min = temperatura_3
    else:
        if (temperatura_3 > temperatura_1):
            max = temperatura_3
            min= temperatura_1
        else:
            max = temperatura_3
            min = temperatura_1
promedio = (temperatura_1+temperatura_2+temperatura_3)/3
print('El valor MAXIMO de tempretura es de:  ',max)
print('el valor minimo de tempretura es de:  ',min)
print('El promedio de temperaturas es:  ', promedio)
#lista= [temperatura_1,temperatura_2,temperatura_3]
#print('La mayor temperatuda registrada es: ',max(lista))
#print('La menor temperatura es:  ', min(lista))
#print ('El promedio de temperaturas es:  ',(temperatura_1+temperatura_2+temperatura_3 )/3)