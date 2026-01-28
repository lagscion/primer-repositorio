

def datos():
    print("\n--- REGISTRO DE VENDEDOR ---")
    cedula = int(input(" cédula del vendedor (-1  salir): "))

    if cedula == -1:
        return cedula, None, None, None

    nombre = input("nombre del vendedor: ")
    
    valor_ventas = 0  
    valor_ventas = int(input("valor total de ventas del mes: "))
    
    comision = 0
    comision = 0  

    return cedula, nombre, valor_ventas, comision


# -------- MENÚ DE TIPOS DE VENDEDOR --------
def menu_vend():
    print("""
----------vendedores -----------------
1. Puerta a Puerta
2. Telemercadeo
3. Ejecutivo de Ventas
------------------------------
""")


def leer_respuesta():
    op = input("Seleccione el tipo de vendedor (1-3): ")
    while (not op.isdigit()) or int(op) < 1 or int(op) > 3:
        print("Opción invalida. Intente nuevamente.") 
        op = input("Seleccione el tipo de vendedor (1-3): ")
    return int(op)


# funsiones

def puerta(valor_ventas):
    print("\nTipo de vendedor: Puerta a Puerta")
    # Calcula comisión del 30% 
    comision = int(valor_ventas * 0.20)
    print("Comision generada: $", comision) 
    return comision


def telemercadeo(valor_ventas):
    print("\nTipo de vendedor: Telemercadeo")
    comision = int(valor_ventas * 0.15)
    print("Comision generada correctamentee: $", comision) 
    return comision


def ejecutivo(valor_ventas):
    print("\nTipo de vendedor: Ejecutivo de Ventas")
    comision = int(valor_ventas * 0.25)
    print("Comision generada: $", comision)
    return comision


# progama

def main():
    print("---------------------------")
    print("calcular comisiones ")
    print("-------------------------------")

    total_ventas = 0
    total_comisiones = 0
    total_comision = 0   

    while True:
        cedula, nombre, valor_ventas, comision = datos()

        if cedula == -1:
            break

        print("\nVendedor registrado:", nombre, "| Cédula:", cedula)

        menu_vend()
        op = leer_respuesta()

        if op == 1:
            comision = puerta(valor_ventas)
        elif op == 2:
            comision = telemercadeo(valor_ventas)
        elif op == 3:
            comision = ejecutivo(valor_ventas)

        total_ventas += valor_ventas
        total_comisiones += comision

        print("--------------------------------------")
        print("Registro completado .")
        print("--------------------------------------")


    print("\n *  total  *")
    print("Total de ventas del mes: $", total_ventas)
    print("Total a pagar en comisiones: $", total_comisiones)
    print("------------------------------------")
    print ("esot es todo amigos")


main()
