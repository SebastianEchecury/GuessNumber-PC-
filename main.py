import random
import time

def adivinar():
    print('Para comenzar ingresa el rango hasta del numero a ingresar: ', end="")
    rangoHasta = int(input())
    print('Ingresa numero a adivinar: ', end="")
    numero = int(input())
    intentos = 1
    numerosIntentados = set()
    encontro = False

    while encontro == False:
        n = random.randrange(1, rangoHasta)
        if not n in numerosIntentados:
            if n == numero:
                print('La maquina intento con ' + str(n))
                print('La maquina adivino en ' + str(intentos) + ' intentos.')
                encontro = True
                break
            else:
                print('La maquina intento con ' + str(n))
                numerosIntentados.add(n)
        intentos = intentos + 1
        time.sleep(2)


print('Bienvenido al Adivinador de Numeros')
print('El juego consiste en ingresar un numero y que la maquina lo adivine')
print()

adivinar()