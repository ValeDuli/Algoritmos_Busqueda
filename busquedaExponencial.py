def busqueda_binaria(lista, inicio, fin, objetivo):
    while inicio <= fin:
        medio=(inicio+fin)//2
        if lista[medio]==objetivo:
            return print(f'El elemento {objetivo} está en el índice {medio}')
        elif lista[medio]<objetivo:
            inicio=medio+1
        else:
            fin=medio-1
    return print(f'El elemento {objetivo} no esta en la lista')

def busqueda_exponencial(lista, objetivo):
    if lista[0]==objetivo:
        return print(f'El elemento {objetivo} está en el índice {0}')
    
    #Encuentra el rango en el cual puede estar el objetivo
    i=1
    while i<len(lista) and lista[i] <= objetivo:
        i*=2
        
    #Realizar una busqueda binaria en el rango determinado
    return busqueda_binaria(lista, i//2, min(i,len(lista)-1),objetivo)

lista=[2,3,4,10,40,50,70,80,100]
objetivo=int(input("Que numero deseas buscar: "))
busqueda_exponencial(lista,objetivo)
