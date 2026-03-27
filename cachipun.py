from random import randint
jugador = input("Escribe tu jugada (rock, paper, scissors, lizard o spock): ")
compu = ["rock","paper","scissors","lizard", "spock"]
resp_compu = compu[randint(0,4)]
print(f"Tu oponente ha elegido {resp_compu}")
if jugador.lower() == "rock":
    if resp_compu == "scissors" or resp_compu == "lizard":
        print("ganaste")
    if resp_compu == "paper" or resp_compu == "spock":
        print("perdiste")
    if resp_compu == "rock":
        print("empate")

elif jugador.lower() == "paper":
    if resp_compu == "rock" or resp_compu == "spock":
        print("ganaste")
    elif resp_compu == "paper":
        print("empate")
    else:
        print("perdiste")

elif jugador.lower() == "scissors":
    if resp_compu == "paper" or resp_compu == "lizard":
        print("ganaste")
    if resp_compu == "rock" or resp_compu == "spock":
        print("perdiste")
    if resp_compu == "scissors":
        print("empate")

elif jugador.lower() == "lizard":
    if resp_compu == "paper" or resp_compu == "spock":
        print("ganaste")
    elif resp_compu == "lizard":
         print("empate")
    else:
        print("perdiste")

elif jugador.lower() == "spock":
    if resp_compu == "scissors" or resp_compu == "rock":
        print("ganaste")
    elif resp_compu == "spock":
         print("empate")
    else:
        print("perdiste")