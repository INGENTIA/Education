'''
lista = [1, 12, 3, 4, 5, 6, 7]

n = len(lista)
print(n)

medio = n // 2
print(medio)

izq = lista[:medio]
print(izq)

der = lista[medio:]
print(der)
'''
'''
for i in range(n):
    print (i)
    for j in range(0, n - i - 1):
        print(f'{i} and {j}')

'''

def ordenamiento_por_mezcla(lista):
    if len(lista) > 1:
        print(lista)
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista[medio: ]
        print(izquierda, '*'*5, derecha)

        #llamada recursiva en cada mitad
        ordenamiento_por_mezcla(izquierda)

        print(f'izquierda {izquierda}, derecha {derecha}')
        print(lista)
        print('-'*50)

    return lista 
olle = [1,5,7,9]
lista = ordenamiento_por_mezcla(olle)
#print(lista)