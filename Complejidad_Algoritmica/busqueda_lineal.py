import random

def busqueda_lineal(lista, objetivo):
    match = False
    counter = 0
    for elemento in lista:
        counter += 1
        if elemento == objetivo:
            match =  True
            break
    print(f'el numero de interacciones en la busqueda lineal fueron {counter}')

    return match

if __name__ == '__main__':
    
    tamano_de_lista = int(input('De que tamano sera la lista?'))
    objetivo = int(input('Que numero quieres entontrar'))

    lista = [random.randint(0, 100) for i in range (tamano_de_lista)]

    encontrado = busqueda_lineal(lista, objetivo)
    print(lista)
    print(f'El elemento objetivo {objetivo} {"esta" if encontrado else "no esta"} en la lista')
    