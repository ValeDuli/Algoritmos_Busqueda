def busqueda_ternaria(lista, objetivo):
    inicio=0
    fin=len(lista)-1
    
    while inicio <=fin:
        tercio1=inicio+(fin-inicio)//3
        tercio2=fin-(fin-inicio)//3
        
        if lista[tercio1]==objetivo:
            return print(f'El elemento {objetivo} está en el índice {tercio1}')
        if lista[tercio2]==objetivo:
            return print(f'El elemento {objetivo} está en el índice {tercio2}')
        
        if objetivo < lista[tercio1]:
            fin=tercio1-1
        elif objetivo > lista[tercio2]:
            inicio=tercio2+1
        else:
            inicio=tercio1+1
            fin=tercio2-1
            
    return print(f'El elemento {objetivo} no esta en la lista')

lista=[10,20,30,40,50,60,70,80,90,100]
objetivo=int(input("Que numero deseas buscar: "))
busqueda_ternaria(lista,objetivo)