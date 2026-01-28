print ("\n")
codigo_estudiante = input ("ingrese el codigo del estudiante: ")
print ("\n")
nombre_del_estuidiante = input ("nombre del estudiante: ")

TEC_SIST = 800_000
TEC_DES_VID = 1_000_000
TEC_ANIM_DIG = 1_200_000
valor_fin = 0



# menu de los cursos 

def menu():
    print ("\n")
    print ("""***     CURSOS A APLICAR  ***

1: Técnico en Sistemas

2: Técnico en Desarrollo de videojuegos

3: Técnico en Animación Digital

4: salir

--------
OPCION (1-4)?""")


# menu de las becas 


def menuBec ():
    print ("\n")
    print ("""  ***  OPCIONES DE BECA   *** 
           
1: Beca por rendimiento académico: Descuento del 50% sobre el valor matricula.
           
2: Beca Cultural - Deportes: Descuento del 40% sobre el valor matrícula.
           
3: Sin Beca.
           
""")













def leer_opcion():
   op =  (input("digite su opcion: "))
   while ( not op.isdigit() ) or int (op) < 1 or int (op) > 4:
       print ("Error. Digite un numero del 1 a el 4. ")
       input ("presione cualquier tecla para continuar....")
       print ("\n\n")
       menu()
       op = input()
   return int (op)


def main():
    opcion = 0
    while (opcion != 4):
        menu()
        opcion = leer_opcion()
        if opcion == 1:
            valor_fin = 0
            opcion = 0 
            menuBec() 
            opcion = leer_opcion()
            if opcion == 1:
                valor_fin = int (TEC_SIST * (50/100))
                print ("\n")
                print ("el estudiante: ", nombre_del_estuidiante, "con el codigo: ", codigo_estudiante, "paga: ",valor_fin)










main()


