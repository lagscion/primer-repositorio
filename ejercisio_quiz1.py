
while  True :
    try:
        capital = int(input("ingrese su capital: "))

        interes = float(input("ingrese la tasa de su interes entre 0% y 100%: "))

        años = int (input("en cuantos años piensas pagarlo: "))

        if  0 <= interes  <= 100 and 0 < capital and 0 < años:
            break

        else:
            print("el valor ingresado no es valido")

    except ValueError:
        print("el valor ingresado no es valido")


interes_acum = 0 
capital_acum = capital

for i in range (años):
    interes_acum = capital_acum * (interes /100)
    capital_acum = capital_acum + interes_acum


print ("su capital final es: ", int(capital_acum))


