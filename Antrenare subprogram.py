def creare_lista():
    n = int(input("nr. de elemente "))
    lista_locala = []
    for i in range(n):
        elem = eval(input("Elementul "+str(i)+' este:'))
        if isinstance(elem, int)==True or isinstance(elem, float):
            lista_locala.append(int(elem))
        else: 
            print(elem+" nu este numar intreg")
    return lista_locala

lista1 = creare_lista()
print(lista1)