# While
# While <Condicipon verdadera>:
#       cuerpo del ciclo
# Condiciones son: expresiones booleanas (or, and) y operaciones de comparación 
# Para controlar un ciclo while
# Ciclos controlados por un contador 
# Variales y evertos 


#i = 0

#while i < 10:
 #   print ("ciclo")
    # Importante modificar el valor del contador 
  #  i = i + i 
    #i+ =1     Es lo mismo

#import random
#a = 0

#while a != 5:
#    a = random.randint(1,10)
#    print (a)
#print("Se acabó")


#while 1 == 1:
    
#    a = int(input("Ingrese un número"))
    
#    if a == 10:
#        break
    

# for: se utiliza para recorrer un "iterable"
# lista, tupla, diccionario...

# Lista: Conjunto de variables organizadas en 
# espacios consecutivos de memoria. A las que 
# se les asigna un unico nomnbre. Se diferencian 
# por la posición que ocupan respecto al primer 
# elemento de la lista 

miLista = [5,45,89,6, 7]

# Estructura del for en python
# for <variable_donde_guardo_el_elemento in iterable>

for x in miLista:
    print (x)
    if x > 50:
        print("grande")
        
# Si solo utilizo el iterable para definor la cantidad 
# de repeticiones entonces n es necesaria la variable 


for _ in miLista:
    print ("ciclo")
# Revisa cuantes veces ser repite el ciclo



miLista2 = []

# En python todos son objetos 

print (len(miLista))

# Tupla: Lista inmutable
# No se puede cambiar

miTupla = (2,45,8,78,9)

# for: Ciclo para recorrer iterables. El cuerpo 
# se repite tantas veces como elementos tenga el
# iterables. En cada ciclo se guarda 






# Si no tengo un iterable puedo usar la función 
# range() para generar una secuencia de números

for x in range(10):
    print (x)

# Imprime de 0 a 9, es decir, 10 numeros 


# Crear un programa que pida un numero al usuario y:
# 1. imprima los numeros impares entre -numero y numero 
# 2. imprima los numeros primos entre 0 y numero*100
# El programa debe garantizar que el usuario ingrese un numero postivo > 0

