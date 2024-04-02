def es_primo(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

while True:
    try:
        numero = int(input("Por favor, ingresa un número entero positivo mayor que 0: "))
        if numero > 0:
            break
        else:
            print("Error: El número debe ser un entero positivo mayor que 0. Intenta de nuevo.")
    except ValueError:
        print("Error: Debes ingresar un número entero válido. Intenta de nuevo.")

# Imprimir los números impares entre -numero y numero
print("Números impares entre -{} y {}:".format(numero, numero))
for i in range(-numero, numero + 1):
    if i % 2 != 0:
        print(i, end=" ")

# Imprimir los números primos entre 0 y numero*100
limite_superior = numero * 100
print("\nNúmeros primos entre 0 y {}:".format(limite_superior))
for num in range(2, limite_superior + 1):
    if es_primo(num):
        print(num, end=" ")
