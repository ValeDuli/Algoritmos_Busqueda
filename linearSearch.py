def busqueda_lineal(lista,objetivo):
    for i in range(len(lista)):
        if lista[i]==objetivo:
            return print(f'El elemento {objetivo} esta en el indice {i}')
    return print(f'El elemento {objetivo} no esta en la lista') #Devuelve -1 si no se encontra el elemento

lista=[2,4,6,8,10]
objetivo= int(input("Que numero deseas buscar: "))
busqueda_lineal(lista, objetivo)