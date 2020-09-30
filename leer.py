lista1 = ['Este','texto','no','concuerda','por','que','esta','mal']
#En la línea 3 va la ruta o el archivo de texto. 
archivo = open("texto.txt")
lista2 = archivo.read().split(' ')

def bubbleString(array,array2):
    length = len(array) - 1 

    #Recorre
    for i in range(0, length):
        #print(f"pasada #{i + 1}")
        #Compara
        for j in range(0, length):
            #print(f"comparacion: {array[j]} > { array[j+1] }")
            if array[j] == array2[j]:
                aux = array2[j]
                array2[j] = array2[j+1]
                array2[j+1] = aux
    return array
                
        
print("Antes de ordenar:")
print(lista2)
print("Despues de ordenar")        
print(bubbleString(lista1, lista2))