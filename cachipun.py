from random import randint
jugador = input()
compu = ["Rock","Paper","Scissors","Lizard", "Spock"]
resp_compu = compu[randint(0,5)]
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