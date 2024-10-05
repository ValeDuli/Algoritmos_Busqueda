def busqueda_binaria(lista, objetivo):
    inicio=0
    fin=len(lista)-1
    while inicio<=fin:
        medio=(inicio+fin)//2
        if lista[medio]==objetivo:
            return print(f'El elemento {objetivo} esta en el índice {medio}')
        elif lista[medio]<objetivo:
            inicio=medio+1
        else:
            fin=medio-1
    return print(f'El elemento {objetivo} no esta en la lista')

lista=[2,4,6,8,10]
objetivo = int(input("Que numero deseas buscar: "))
busqueda_binaria(lista,objetivo)
