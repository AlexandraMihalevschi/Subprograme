def creare_lista():
    n = int(input("nr. de elemente "))
    lista_locala = []
    for i in range(n):
        elem = eval(input("Elementul "+str(i)+' este:'))
        if isinstance(elem, float)==True:
            lista_locala.append(float(elem))
        else: 
            print("Elementul "+str(i)+" nu este numar intreg")
    return lista_locala

lista1 = creare_lista()
print(lista1)
