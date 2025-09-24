def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(n - 1 - i):  
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# Programa principal
texto = input("Digite uma string: ")

# Converte string em lista de caracteres
lista = list(texto)

# Ordena com bubble sort
ordenada = bubble_sort(lista)

# Junta de volta em string
resultado = "".join(ordenada)

print("String ordenada:", resultado)
