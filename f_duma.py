# hacer una función que sume dos numeros

def suma(num1, num2):
    return num1 + num2

n1 = int(input("numero 1? "))
n2 = int(input("numero 2? "))

s = suma(n1, n2)
print(f"La suma de {n1} y {n2} es {s}")