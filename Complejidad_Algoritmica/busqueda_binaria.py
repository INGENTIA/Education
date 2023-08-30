
import random
#Busqueda lineal
def busqueda_lineal(lista, objetivo, iterlin=0):
    match = False
    for elemento in lista:
        iterlin += 1
        if elemento == objetivo:
            match =  True
            break
    

    return (match, iterlin)
    
#Busqueda Binaria
def busqueda_binaria(lista, comienzo, final, objetivo,iterbin= 0):

	iterbin += 1
	
	#print (f'buscando {objetivo} entre {lista[comienzo]} y {lista[final - 1]}')	
	if comienzo > final:
		return (False, iterbin)

	medio = (comienzo + final ) // 2

	if lista[medio] == objetivo:
		return (True, iterbin)
	elif lista[medio] < objetivo:
		return busqueda_binaria(lista, medio + 1, final, objetivo, iterbin = iterbin)  
	else:
		return busqueda_binaria(lista, comienzo, medio - 1, objetivo, iterbin =iterbin) 

	


if __name__ == '__main__':
	tamano_de_lista = int(input('De que tamano es la lista'))
	objetivo = int(input('Que numero quieres encontrar?'))

	lista = sorted([random.randint(0, 100) for i in range(tamano_de_lista)])

	(encontrado1, iterbin) = busqueda_binaria(lista, 0, len(lista), objetivo)
	(encontrado2, iterlin) = busqueda_lineal(lista, objetivo)

	counter = 1

	print(lista)
	print(f'Binaria: El elemento {objetivo}{"esta" if encontrado1 else "no esta"} en la lista')
	print(f'Lineal: El elemento {objetivo}{"esta" if encontrado2 else "no esta"} en la lista')
	print(f'El numero de iteraciones de la busqueda lineal fueron: {iterlin}')
	print(f'El numero de iteraciones de la busqueda binaria fueron: {iterbin}')