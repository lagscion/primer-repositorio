
def main ():
    saldo = 0
    op = 0
    while op != 5:
        menu ()
        op = leer_opcion()
        if op ==  1:
            saldo = saldo + monto()
            print ("su nuevo saldo es de: ", saldo)
        elif op == 2:
            saldo = saldo - paga(saldo)
        elif op == 3:
            saldo = saldo - transferir (saldo)
        elif op == 4:
            mostrar (saldo)

    print ("gracias por usar nequi")



def mostrar (saldo):
    print (saldo)


def monto ():
    monto = (input("ingrsese el monto a reccargar: "))
    while ( not monto.isdigit() ) or int (monto) <= 0 :
        print ("Error. Digite un NUMERO mayor a 0. ")
        input ("presione cualquier tecla para continuar....")
        print ("\n\n")
        menu()
        monto = input()
    return int (monto)



def paga (saldo):
    paga = (input("ingrsese el monto a reccargar: "))
    while ( not paga.isdigit() ) or int (paga) <=0 or saldo < int(paga) :
        print ("Error. Digite un NUMERO valido. ")
        input ("presione cualquier tecla para continuar....")
        print ("\n\n")
        menu()
        paga = input()
    return int (paga)


def transferir (saldo):
    num_dest = (input("ingrese el numero del destinatario: "))
    transferencia = (input("ingrese el valor de la transferencia: "))

    while  (not num_dest.isdigit()) or len(num_dest) != 10:  
        print ("Error. Digite un NUMERO valido. ")
        input ("presione cualquier tecla para continuar....")
        print ("\n\n")
        menu()
        num_dest= input()
    while (not transferencia.isdigit()) or int (transferencia) <=0 or int(transferencia) > saldo:
        print ("Error. saldo insuficiente. ")
        input ("presione cualquier tecla para continuar....")
        print ("\n\n")
        menu()
        transferencia = input()
    return int (transferencia)










def menu():
    print ("\n")
    print ("""***    NEQUI  ***

1. Cargar saldo

2. Pagar

3. Transferir dinero

4. Mostrar saldo

5. Salir

--------
OPCION (1-5)?""")
    

def leer_opcion():
    op =  (input("digite su opcion: "))
    while ( not op.isdigit() ) or int (op) < 1 or int (op) > 5:
        print ("Error. Digite un numero del 1 a el 5. ")
        input ("presione cualquier tecla para continuar....")
        print ("\n\n")
        menu()
        op = input()
    return int (op)

main()