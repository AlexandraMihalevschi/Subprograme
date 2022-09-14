def creare_lista():
    n = int(input("nr. de elemente "))
    lista_locala = []
    for i in range(n):
        elem = eval(input("Elementul "+str(i)+' este:'))
        if isinstance(elem, int)==True:
            lista_locala.append(int(elem))
        else: 
            return
    return lista_locala

lista1 = creare_lista()
print(lista1)
