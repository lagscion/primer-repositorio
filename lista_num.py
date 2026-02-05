numeros = input ("ingrese sus numeros separandolos por espacios: ")



lista = numeros.strip(" ").strip (",").split(" ")

for i in range (len(lista)):
    lista [i] = int (lista[i])    


lista.sort( reverse = True )
print ("el numero mayor de la lista es", lista[0], "y el menor es", lista[-1])

prom_list = 0 

for i in range (len(lista)):
    prom_list =  int(lista[i]) + prom_list


print  ("su promedio es: ",  int(prom_list/ len(lista)))

par = 0 
impar = 0 


for i in range (len(lista)):
    if int(lista[i]) % 2 == 0:
        par += 1
    else:
        impar += 1

print ("total numeros pares: ",par,"\n","total numeros impares: ", impar)

