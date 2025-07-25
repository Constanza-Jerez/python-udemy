num_pares = [1,2,3,4,5,6,7,8,9,10]
lista = []

for n in num_pares:
    #print(n)
    if n % 2 == 0:          #si la variable n es igual a 0, es decir, se divide n en 2 y si el residuo de la division es igual a 0 el numero es par
        lista.append(n)
print(lista)