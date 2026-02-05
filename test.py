def main ():
    saldo = 1000
    op = 0
    while op != 4 :
        
        menu ()
        op = leer_opcion()
        
        if op == 0:
            break
        elif op ==  1:
            consultarSaldo (saldo)
        elif op == 2:
            saldo = saldo  + depositar () 
        elif op == 3:
            saldo = saldo - retirar(saldo)

    print ("\n","gracias por usar este cajero...","\n")

#consultar saldo

def consultarSaldo (saldo):
    print ("\n", "su saldo actual es de: ", saldo)

#depositar

def depositar ():
    depositar = (input("ingrsese el monto a depositar: "))
    while ( not depositar.isdigit() ) or int (depositar) <= 0 :
        print ("Error. Digite un NUMERO mayor a 0. ")
        input ("presione cualquier tecla para continuar....")
        print ("\n\n")
        menu()
        depositar = input()
    return int (depositar)

#retirar

def retirar (saldo):
    retirar = (input("ingrsese el monto a retirar: "))
    while ( not retirar.isdigit() ) or int(retirar) <=0 or saldo < int(retirar) :
        print ("Error. Digite un NUMERO valido. ")
        input ("presione cualquier tecla para continuar....")
        print ("\n\n")
        menu()
        retirar = input()
    print ("su reitro se ha hecho con exito.")
    return int (retirar)

#menu

def menu():
    print ("\n")
    print ("""***    cajero  ***

1. Consultar saldo 

2. depositar dinero

3. retirar dinero 

4. salir

--------
OPCION (1-4)?""")

#leer opcion

def leer_opcion():
    op =  (input("\n""digite su opcion: "))
    while ( not op.isdigit() ) or int (op) < 0 or int (op) > 4:
        print ("Error. Digite un numero del 1 a el 4. ")
        input ("presione cualquier tecla para continuar....")
        print ("\n\n")
        menu()
        op = input()
    return int (op)

main()