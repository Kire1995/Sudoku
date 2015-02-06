archivo=open ("sudoku_vslido.txt","r")
lineas=archivo.readlines()
lista=[]
for x in range (0,9):
    for y in range (0,9):
        lista = lista+ int(lineas[x][2*y:2*y+1])
print(lista)


def validacion(lista):
    for x in range(1,10):
        if 1!=lista.count(x):
            return false
    return true
