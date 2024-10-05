def busqueda_ternaria(lista, inicio, fin, objetivo):
    if inicio > fin:
        return print(f'El elemento {objetivo} no esta en la lista') #El objetivo no se encuentra en la lista
    
    #Encuentra los dos puntos medios
    tercio1=inicio+(fin-inicio)//3
    tercio2=fin-(fin-inicio)//3
    
    #Comprueba los puntos medios
    if lista[tercio1]==objetivo:
        return print(f'El elemento {objetivo} está en el índice {tercio1}')
    if lista[tercio2]==objetivo:
        return print(f'El elemento {objetivo} está en el índice {tercio2}')
    
    #Divide la lista en tres partes
    if objetivo<lista[tercio1]:
        return busqueda_ternaria(lista, inicio, tercio1-1, objetivo)
    elif objetivo>lista[tercio2]:
        return busqueda_ternaria(lista,tercio2+1,fin,objetivo)
    else:
        return busqueda_ternaria(lista,tercio1+1,tercio2-1,objetivo)
    
lista=[2,4,6,7,10,12,14,16,18,20]
objetivo=int(input("Que numero deseas buscar: "))
busqueda_ternaria(lista,0,len(lista)-1,objetivo)