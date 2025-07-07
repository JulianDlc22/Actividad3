def menu():
    print("---MENU---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Salir")

while True:
    menu()
    opcion = int(input("Ingresa una opcion: "))
    match opcion:
        case 1:
            numero = int(input("Ingresa el primer numero: "))
            numero2 = int(input("Ingresa el segundo numero: "))
            suma = numero + numero2
            print("El resultado es: ", suma)
        case 2:
            numero = int(input("Ingresa el primer numero: "))
            numero2 = int(input("Ingresa el segundo numero: "))
            resta = numero - numero2
            print("El resultado es: ", resta)
        case 3:
            print("Gracias por usar el programa")
            break


