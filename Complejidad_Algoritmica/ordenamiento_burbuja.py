import random

def ordenamiento_de_burbuja(lista, count=0):
    
    n =len(lista)

    for i in range(n):
        count +=1
        for j in range(0, n - i - 1):
        
            if lista[j] > lista [j + 1]:
                lista[j] , lista[j + 1]  = lista[j+ 1], lista[j]
                print(lista)

            count += 1
            print(count)

    return lista

if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamano sera la lista'))

    lista = [random.randint(0,100) for i in range(tamano_de_lista)]
    print(f'la lista es : {lista}')

    lista_ordenada = ordenamiento_de_burbuja(lista)
    print(f'la lista ordenada es : {lista_ordenada} ')