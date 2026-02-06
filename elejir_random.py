import random
turnos = 0

numero = random.randint(1, 1000)

numero_adiv = 0 

for i in range (1, 11):
    numero_adiv = int(input("elige un numero: "))
    turnos +=1 
    if numero_adiv < numero:
        print("Pista: el numero secreto  es mayor")
    
    elif numero < numero_adiv:
        print ("Pista:  el numero secreto es menor")
    
    elif numero == numero_adiv:
        print (f"felicidades encontraste el numero {numero} y te tardo encontrarlo unos {turnos} turnos.")
        break

if numero_adiv != numero:
    print(f"se te acabaron los intentos, el numero era {numero}")