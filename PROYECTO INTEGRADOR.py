import random
print ('¡BIENVENIDO!')
nombre = (input('Porfavor, ingrese su nombre:'))
print ('Hola', nombre)
while (True):
    print ('''Porfavor seleccione el juego que desee ejecutar:
    1) Piedra, papel o tijeras
    2) Adivinar un numero compitiendo contra la computadora
    3) Tirar un dado
    4) Graficar una función''')
    opcion = input()
    if opcion == '1':
     while True:
            aleatorio = random.randrange(0, 3)
            elijePc = ''
            print ('1) Piedra')
            print ('2) Papel')
            print ('3) Tijera')
            opcion = int(input('Elige tu opcion:'))

            if opcion == 1:
                elijeUsuario = 'Piedra'
            elif opcion == 2:
                elijeUsuario = 'Papel'
            elif opcion == 3:
                elijeUsuario = 'Tijera'
            print ('Elejiste: ', elijeUsuario)

            if aleatorio == 0:
                elijePc = 'Piedra'
            elif aleatorio == 1:
                elijePc = 'Papel'
            elif aleatorio == 2:
                elijePc = 'Tijera'
            print ('La maquina elijio: ', elijePc)
            print ('. . .')
            if elijePc == 'Piedra' and elijeUsuario == 'Papel':
                print ('Ganaste!')
            elif elijePc == 'Papel' and elijeUsuario == 'Tijera':
                print ('Ganaste!')
            elif elijePc == 'Tijera' and elijeUsuario == 'Piedra':
                print ('Ganaste')
            if elijePc == 'Piedra' and elijeUsuario == 'Tijera':
                print ('Perdiste :(')
            elif elijePc == 'Papel' and elijeUsuario == 'Piedra':
                print ('Perdiste :(')
            elif elijePc == 'Tijera' and elijeUsuario == 'Papel':
                print ('Perdiste :(')
            elif elijePc == elijeUsuario:
                print ('Se produjo un empate')

            print ('''Quieres jugar de nuevo? Porfavor, seleccione el numero correspondiente a su respuesta:
            1) Si
            2) No''')
            jugar_de_nuevo = input ()
            if jugar_de_nuevo == '2':
                break
          
    if opcion == '3':
            while True:
                prediccion = int(input('Porfavor, ingrese su prediccion acerca de que número saldra: '))
                resultado = random.randint(1,6)
                print ('El dado giro... obtuvo:', resultado)
                if resultado > prediccion:
                    print ('Tu prediccion fue: erronea :(')
                elif resultado < prediccion:
                    print ('Tu prediccion fue: erorrena :(')
                elif resultado == prediccion:
                    print ('Tu prediccion fue: acertada :)')
                input ('Presiona doble "enter" para jugar nuevamente. Si no desea jugar nuevamente, presione enter, luego "n" y luego enter  nuevamente')
                jugar_de_nuevo = input ()
                if jugar_de_nuevo == 'n':
                    break
                
    if opcion == '2':
            numero = random.randint(1,10)
            intentos = 0
            print ('Muy bien,', nombre, 'estoy pensando en un numero entre el 1 y el 10, intenta adivinarlo')
            while True:
                aproximacion = int(input ('Ingrese su numero: '))
                intentos = intentos +1
                if aproximacion > numero:
                   print ('Incorrecto... Intenta con un numero mas chico.')
                if aproximacion < numero:
                   print ('Incorrecto... Intenta con un numero mas grande.')
                if aproximacion == numero:
                   print ('Muy bien,', nombre, '! Has acertado en el intento numero', intentos,'''. ¿Deseas jugar de nuevo? Porfavor selecciona el numero que corresponda a tu respuesta:
                   1) Si
                   2) No''')
                   jugar_de_nuevo = input ()
                   if jugar_de_nuevo == '2':
                       break

    if opcion == '4':
       import matplotlib.pyplot as plt
import numpy as np


fig, ax = plt.subplots()
ax.spines[["left", "bottom"]].set_position(("data", 0))
ax.spines[["top", "right"]].set_visible(False)

ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

x = np.linspace(-0.75, 3, 20)
ax.plot(x, np.sin(x*np.pi))

plt.show()
