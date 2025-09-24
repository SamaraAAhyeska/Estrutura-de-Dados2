def selection_sort_decrescente(vetor):
    n = len(vetor)
    for i in range(n - 1):
        max_idx = i                     
        for j in range(i + 1, n):       
            if vetor[j] > vetor[max_idx]:
                max_idx = j           
        if max_idx != i:                
            vetor[i], vetor[max_idx] = vetor[max_idx], vetor[i]
    return vetor



v = [5, 2, 9, 1, 7, 3]
print("Vetor original:", v)
resultado = selection_sort_decrescente(v)
print("Vetor em ordem decrescente:", resultado)
