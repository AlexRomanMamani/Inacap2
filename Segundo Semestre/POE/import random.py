import random
ri = 1  # rango inicial random
rf = 10  # rango final random
r1 = random.randint(1, 10)  # genera un valor entero aleatorio
x = 5  # intentos
xi = x  # intentos inicial
n = 1  # numero a adivinar
p = 100  # puntuacion
pi = p  # puntuacion inicial
op = 0  # opción


def juego(n, x, r1, p):
    while n != 0 and x >= 1:
        n = int(
            input("Ingrese número a adivinar (0 Salir), (puntuacion:" + str(p) + "):"))
        if n == 0:
            print("Gracias por jugar\nHasta la próxima.")
            break
        if n == r1:
            if x-1 == 0:
                print("¡¡gano!! ¡y en el ultimo intento!")
            elif x-1 == 1:
                print("¡¡gano!! y aun te quedaba " + str(x-1) + " intento.")
            else:
                print("¡¡gano!! y aun te quedaban " + str(x-1) + " intentos.")
            print("Su puntuacion es: " + str(p))
            break
        if n < r1:
            if x-1 == 0:
                print("Lastima, ese era el ultimo intento")
                if x-1 == 1:
                    print("falta, te queda " + str(x-1) + " intento.")
            else:
                print("falta, te quedan " + str(x-1) + " intentos")
            p = p-(pi // xi)
        if n > r1:
            if x-1 == 0:
                print("Lastima, ese era el ultimo intento")
                if x-1 == 1:
                    print("te pasaste, te queda " + str(x-1) + " intento.")
            else:
                print("te pasaste, te quedan " + str(x-1) + " intentos.")
            p = p-(pi // xi)
        x = x-1
    else:
        print("***** Perdiste *****")
        print("El numero era " + str(r1))


def menu():
    print("\n******************************************")
    print("Bienvenido al juego de adivinar el número.\n")
    print("Configuración actual: \nIntentos: " +
          str(x) + "\nDificultad: Facil (adivinar número desde el " + str(ri) + " hasta " + str(rf) + ")\n")

    print("1: Jugar".center(18, " "))
    print("2: Configurar y Jugar".center(32, " "))
    print("3: Salir\n".center(20, " "))


menu()
op = int(input("Ingrese opción: "))


if op == 1:

    while op == 1:
        r1 = random.randint(1, 10)
        juego(n, x, r1, p)
        op = int(input("Desea seguir jugando? (1: Si 2: No)"))
    else:
        print("Gracias por jugar\nHasta la próxima.")
elif op == 2:
    print("\n********** Configurar y Jugar **********\n")
    print("Intentos:")
    x = int(input("Ingrese cantidad de intentos: ".center(20, " ")))
    xi = x
    print("Dificultad:\nFacil: adivinar número desde el 1 hasta 10\nDificil: adivinar número desde el 1 hasta 100 \n")
    op = int(input("Ingrese opción (1-2)"))
    if op == 1:
        ri = 1
        rf = 10
        r1 = random.randint(ri, rf)
        juego(n, x, r1, p)
    elif op == 2:
        ri = 1
        rf = 100
        r1 = random.randint(ri, rf)
        juego(n, x, r1, p)
else:
    print("Gracias por jugar\nHasta la próxima.")
