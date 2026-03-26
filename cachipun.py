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



if jugador.lower()== "paper":
    if resp_compu == "spock" or resp_compu == "rock":
        print("ganaste")
    if resp_compu == "scissors" or resp_compu == "lizard":
        print("perdiste")
    if resp_compu == "paper":
        print("empate")

if jugador.lower() == "scissors":
    if resp_compu == "paper" or resp_compu == "lizard":
        print("ganaste")
    if resp_compu == "rock" or resp_compu == "spock":
        print("perdiste")
    if resp_compu == "scissors":
        print("empate")

if jugador.lower()
