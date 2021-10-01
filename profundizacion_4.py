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

# Ejercicios de práctica con texto
'''
Enunciado:
Realice un programa que solicite por consola 3 palabras cualesquiera
Luego el programa debe consultar al usuario como quiere ordenar las palabras
1 - Ordenar por orden alfabético (usando el operador ">")
2 - Ordenar por cantidad de letras (longitud de la palabra (len) y operador ">")

Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
e imprimir en pantalla de la mayor a la menor

Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
e imprimir en pantalla de la mayor a la menor

IMPORTANTE: Para ordenar las palabras deben realizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido.
'''

print('Ejercicios de práctica con cadenas')
# Empezar aquí la resolución del ejercicio
palabra_1 = str(input('Ingrese primera palabra: '))
palabra_2 = str(input('Ingrese segunda palabra: '))
palabra_3 = str(input('Ingrese tersera palabra: '))
letras_1 = len(palabra_1)
letras_2 = len(palabra_2)
letras_3 = len(palabra_3)

opcion = int(input('Ingrese 1 si desea ordenarlas por orden alfabetico y 2 por orden numerico:  '))
if (opcion == 1):
    if (palabra_1 > palabra_2) and (palabra_2 > palabra_3):
        if (palabra_2) > (palabra_3):
            print('Las palabras ordenadas alfabeticamente son: ', palabra_1,palabra_2, palabra_3)
        else:
            if(palabra_3 > palabra_2):
                print('Las palabras ordenadas alfabeticamente son: ', palabra_1,palabra_3,palabra_2)
    else:
        if(palabra_1 < palabra_2) and (palabra_1 < palabra_3):
            print ('Las palabras ordenadas alfabeticamente son: ', palabra_2, palabra_3, palabra_1)
        else:
            if (palabra_2 < palabra_3):
                print ('Las palabras ordenadas alfabeticamente son: ', palabra_3, palabra_2, palabra_1)
else: 
    if(opcion == 2 ):
        if (letras_1 > letras_2) and (letras_2 > letras_3):
           if (letras_2) > (letras_3):
            print('Las palabras ordenadas numericamente son: ', letras_1, letras_2, letras_3)
        else:
            if(letras_3 < letras_2):
                print('Las palabras ordenadas numericamente son: ', letras_2, letras_1 ,letras_3)
    else:
        if(letras_1 < letras_2) and (letras_1 < letras_3):
            print ('Las palabras ordenadas numericamente son: ', letras_2, letras_3, letras_1)
        else:
            if (letras_3 > letras_2):
                print ('Las palabras ordenadas numericamente son: ', letras_3, letras_2, letras_1)
print('fin de programa')