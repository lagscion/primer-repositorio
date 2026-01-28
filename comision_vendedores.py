def main ():
    while (cedula != -1 ):
        menu_vend()
        op = leer_respuesta ()
        if op == 1:
            puerta()
        elif op == 2:
            telemercadeo()
        elif op == 3: 
            ejec_ventas()













def leer_respuesta ():
    op = (input ("ingrese la clase de vendedor:""\n"))
    while ( not op.isdigit() ) or int (op) < 1 or int (op) > 4:
        print ("numero invalido, intententelo denuevo.""\n" )
        input ("presione cualquier tecla para continuar... ")
        print ("\n\n")
        print (menu_vend())
        op = input()
    return int (op)

def menu_vend():
    print ("""*** TIPOS DE VENDEDORES ***

1: Puerta a Puerta

2: Telemercadeo

3: Ejecutivo de ventas

""")



def puerta():
    print ("el vendedor es: vendedor de puerta en puerta. \n")
    comision_puerta = int(valor_ventas * (20/100))
    print ("la comision es de: ", comision_puerta)
    print ("\n")

def telemercadeo ():
    print ("el vendedor es: vendedor telemercadero. \n")
    comision_tele = int(valor_ventas * (15/100))
    print ("la comision es de: ", comision_tele)
    print ("\n")

def ejec_ventas ():
    print ("el vendedor es: ejecutivo de ventas. \n")
    comision_ejec = int(valor_ventas * (25/100))
    print ("la comision es de: ", comision_ejec)
    print ("\n")

def ejec_ventas ():
    print ("el vendedor es: ejecutivo de ventas. \n")
    comision_ejec = int(valor_ventas * (25/100))
    print ("la comision es de: ", comision_ejec)
    print ("\n")



cedula = int(input("cedula?: "))
nombre = (input("nombre?: "))
valor_ventas = int(input("valor total de las ventas del mes: "))
comision = 0 


main()


