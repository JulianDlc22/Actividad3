def menu():
    print("---MENU---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Salir")

menu()
opcion = int(input("Ingresa una opcion: "))

if opcion == 1:
    numero = int(input("Ingresa el primer numero: "))
    numero2 = int(input("Ingresa el segundo numero: "))
    suma = numero + numero2
    print("El resultado es: ", suma)