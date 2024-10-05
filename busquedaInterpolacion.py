def busqueda_interpolacion(lista, objetivo):
    inicio=0
    fin=len(lista)-1
    
    while inicio<=fin and objetivo>=lista[inicio] and objetivo<=lista[fin]:
        #Evita la division por cero
        if inicio==fin:
            if lista[inicio]==objetivo:
                return print(f'El elemento {objetivo} está en el índice {inicio}')
            return -1
        
        #Fórmula de interpolación
        pos=inicio+((fin-inicio)//(lista[fin]-lista[inicio])*(objetivo-lista[inicio]))
        
        #Verifica si el objetivo esta en la posición calculada
        if lista[pos]==objetivo:
            return print(f'El elemento {objetivo} está en el índice {pos}')
        
        #Ajusta los limites según el valor en la posicion calculada
        if lista[pos]<objetivo:
            inicio=pos+1
        else:
            fin=pos-1
            
    return print(f'El elemento {objetivo} no esta en la lista')

lista=[10,20,30,40,50,60,70,80,90,100]
objetivo=int(input("Que numero deseas buscar: "))
busqueda_interpolacion(lista,objetivo)