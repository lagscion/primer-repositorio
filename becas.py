print ("\n")
codigo_estudiante = input ("ingrese el codigo del estudiante: ")
print ("\n")
nombre_del_estudiante = input ("nombre del estudiante: ")

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




def leer_opcion_bec():
   op =  (input("digite su opcion: "))
   while ( not op.isdigit() ) or int (op) < 1 or int (op) > 3:
       print ("Error. Digite un numero del 1 a el 3. ")
       input ("presione cualquier tecla para continuar....")
       print ("\n\n")
       menu()
       op = input()
   return int (op)








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
    opcion_carrera = 0
    while (opcion_carrera != 4):
        menu()
        opcion_carrera = leer_opcion()

# tecnico en sistemas       

        if opcion_carrera == 1:
            valor_fin = 0
            opcion_beca = 0 
            menuBec() 
            opcion_beca =leer_opcion_bec()

# becas para el tecnico en sistemas

            if opcion_beca == 1:
                valor_fin = int (TEC_SIST - (TEC_SIST * (50/100)))
                print ("\n")
                print ("el estudiante: ", nombre_del_estudiante, "con el codigo: ", codigo_estudiante, "paga: ",valor_fin)
            elif opcion_beca == 2:
                valor_fin = int (TEC_SIST - (TEC_SIST * (40/100)))
                print ("\n")
                print ("el estudiante: ", nombre_del_estudiante, "con el codigo: ", codigo_estudiante, "paga: ",valor_fin)
            elif opcion_beca == 3:
                valor_fin = TEC_SIST
                print ("\n")
                print ("el estudiante: ", nombre_del_estudiante, "con el codigo: ", codigo_estudiante, "paga: ",valor_fin)

# tecnico en desarrollo de videojuegos

        if opcion_carrera == 2:
            valor_fin = 0
            opcion_beca = 0 
            menuBec() 
            opcion_beca = leer_opcion_bec()

# becas para el tecnico en dev video

            if opcion_beca == 1:
                valor_fin = int (TEC_DES_VID - (TEC_DES_VID * (50/100)))
                print ("\n")
                print ("el estudiante: ", nombre_del_estudiante, "con el codigo: ", codigo_estudiante, "paga: ",valor_fin)
            elif opcion_beca == 2:
                valor_fin = int (TEC_DES_VID - (TEC_DES_VID * (40/100)))
                print ("\n")
                print ("el estudiante: ", nombre_del_estudiante, "con el codigo: ", codigo_estudiante, "paga: ",valor_fin)
            elif opcion_beca == 3:
                valor_fin = TEC_DES_VID
                print ("\n")
                print ("el estudiante: ", nombre_del_estudiante, "con el codigo: ", codigo_estudiante, "paga: ",valor_fin)

# tecnico en animacion digital

        if opcion_carrera == 3:
            valor_fin = 0
            opcion_beca = 0 
            menuBec() 
            opcion_beca = leer_opcion_bec()

# becas para el Técnico en Animación Digital

            if opcion_beca == 1:
                valor_fin = int (TEC_ANIM_DIG - (TEC_ANIM_DIG * (50/100)))
                print ("\n")
                print ("el estudiante: ", nombre_del_estudiante, "con el codigo: ", codigo_estudiante, "paga: ",valor_fin)
            elif opcion_beca == 2:
                valor_fin = int (TEC_ANIM_DIG - ( TEC_ANIM_DIG * (40/100)))
                print ("\n")
                print ("el estudiante: ", nombre_del_estudiante, "con el codigo: ", codigo_estudiante, "paga: ",valor_fin)
            elif opcion_beca == 3:
                valor_fin = TEC_ANIM_DIG
                print ("\n")
                print ("el estudiante: ", nombre_del_estudiante, "con el codigo: ", codigo_estudiante, "paga: ",valor_fin)
















main()


