# Programa para jugar piedra papel o tijera con un sistema

from random import*

# input

Jugador = input("A cual te vas: piedra, papel o tijeras: ")

# Processing
opciones = ["piedra","papel","tijeras"]
Maquina = choice (opciones)
if Jugador == Maquina:
    print ("Tu elegiste",Jugador,"y la maquina eligio",Maquina,"asi que tuvieron un empate")

elif(Jugador == "piedra" and Maquina == "tijeras") or (Jugador == "tijeras" and Maquina == "papel") or (Jugador == "papel" and Maquina == "piedra"):
    print ("Tu elegiste",Jugador,"y la maquina eligio",Maquina,"asi que ganaste")

else:
    print ("Tu elegiste",Jugador,"y la maquina eligio",Maquina,"asi que perdiste")