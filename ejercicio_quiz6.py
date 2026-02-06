

suma_de_sueldos = 0
sueldos = 0
sueldo_may = 0
numero_sueldo_mayor = 0
sueldo = 1
numero = 1

while 0 < sueldo:
    numero = int(input("ingrese el numero del trabajador: "))
    if numero > 0 :
        sueldo = int(input("ingrese el sueldo del trabajador: "))
    else:
        
        break
    if sueldo > 0:
        sueldos += 1
        suma_de_sueldos = suma_de_sueldos + sueldo
    else:
        break

    if sueldo_may < sueldo :
        sueldo_may = sueldo 
        numero_sueldo_mayor = numero 


prom = suma_de_sueldos / sueldos

print (f"""el empleado con el numero: {numero_sueldo_mayor} devenga el sueldo mas grande con un valor de {sueldo_may: ,}
        a comparacion con el promedio de los trabajadores que es {prom:,} 
        siendo calculado con un total de {sueldos} sueldos""")
