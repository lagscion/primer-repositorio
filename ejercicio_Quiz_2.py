# 2. ¿Cuáles y cuántos son los números primos comprendidos entre 1 y 1000?. Use el
# algoritmo de la criba de Eratóstenes.
# El algoritmo de la criba de Eratóstenes se puede explicar a tus estudiantes como un
# juego de “ir tachando” números que NO son primos hasta que solo queden los primos.
# i. Se escribe una lista con todos los números desde 2 hasta el límite que se desee
# (por ejemplo, 100).
# ii. Se busca el primer número de la lista que no esté tachado; ese número es primo.
# iii. Se tachan todos los múltiplos de ese número (excepto él mismo).
# iv. Se repiten los pasos 2 y 3 hasta que ya no queden números nuevos para revisar.
# v. Los números que queden sin tachar son los primos.
# Un ejemplo concreto: de 1 a 100 se suele empezar tachando el 1 (no es primo) y luego
# haciendo el proceso desde el 2.



primo = True
no_primo = False

for i in range (2, 10):
    for a in range (2,i):
        if i % a == 0 :
            print (i)


        
        
        

    
    


