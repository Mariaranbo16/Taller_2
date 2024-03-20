# Esto es un comentario de una línea 
# Todo lo que va después es ignorado
# por el interprete de python 

# Variables: Espacio de memoria, con nmbre, donde guardo valores
# Los nombres de variables deben se cortos, descriptivos, NO TENER ESPACIOS
# EN BLANCO ni caracteres especiales, no deben empezar por número

# Descriptivo significa que representa la categoría del dato que quiero guardar
# números (enteros, reales), cadenas de carácteres (string), booleanos (True, False)
# caracteres.

variable = 1

variable = 'Hola'

variable = True

variable = 'a'

variable = 3.14159265365

# Para asignar un valor a la variable se una el operador =



# Operadores: Mecanismo para obtener un dato a partir de otros datos.
# Los datos que intervienen se llaman operadores 

# Aritmeticos: + - / %
# De comparación: Retornan True or False. < > >= <= == !=
# Los de lógica boolana: AND OR. Retornan True o False de a cuerdo a una 
# tabla de verdad. Los operadores siempre son booleanos (True or False)

a = True
b = False 

print (a and b)

# Los operadores booleanos y de comparación son muy utilizados al
# definir condiciones 


# Estructura de contro del código: En general un programa se ejecuta
# línea por línea de forma secuencial. Se puede romper esa secuencialidad 
# empleando un conjunto de sentencias (expresiones) que permite:
# 1. Seleccionar la ejecución de un bloque de código
# 2. Repetir la ejecución de un bloque de código
# 3. Seleccionar entre ejecutar un bloque de código y otro bloque de código
# De esta manera podemos "romper" la secuencialidad
# Principios del paradigma de programación estructurado 

# Sentencia if. Si se cumple una condición (se evalua como True) 
# se ejecuta un bloque de código 

'''
print ("Línea 1")
print ("Línea 2")

if 5>8 or 3<7:
    print ("Esto se muestra si la condición es verdadera")
else:    
    print ("Esto se muestra si la condición es falso")
'''

entrada = int(input("¿Cuántos años tiene? "))

if entrada < 18:
    print ("Es un menor de edad")
else:    
    print ("Ya está grande, deje de chillar")

#Taller: Crear un programa en python que genere un numero aleatorio 
# Entre 2 y 12. Si el numero es 7 imprimir ganó si no imprimir deje el juego