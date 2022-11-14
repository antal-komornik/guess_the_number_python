import random
import os

hit = True
def play():
    global hit
    gen = round(random.random()*100)
    print("Gondoltam egy számara.\nSzerinted melyik az? ")
    while hit:
        num = int(input())
        if gen > num:
            print("a szám amire gondoltam nagyobb mint: ", num)
        elif gen < num:
            print("a szám amire gondoltam kisebb mint: ", num)
        elif gen == num:
            print("GRATULÁLOK, ELTALÁLTAD")
            hit = False
            replay()
        else:
            print("valami hiba történt")
            return

def replay():
    global hit
    b = True
    while b:
        v = input("Szeretnél még egyet játszani? (igen/nem)")
        lower = v.lower()
        if lower not in ["igen", "nem"]:
            print("nem megfelelő szöveg. (igen/nem)")
            continue
        elif lower == "igen":
            b = False
            hit = True
            os.system('cls')
            play()
        else:
            print("Sajnálom!")
            break

play()