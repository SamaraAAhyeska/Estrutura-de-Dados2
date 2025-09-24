def selection_sort_decrescente(vetor):
    n = len(vetor)
    for i in range(n - 1):                 # percorre até o penúltimo elemento
        max_idx = i                        # assume que o maior está em i
        for j in range(i + 1, n):          # percorre o resto do vetor
            if vetor[j] > vetor[max_idx]:  # se achar um maior
                max_idx = j                # atualiza índice do maior
        if max_idx != i:                   # troca só se necessário
            vetor[i], vetor[max_idx] = vetor[max_idx], vetor[i]
    return vetor


# Programa principal (exemplo de uso)
v = [5, 2, 9, 1, 7, 3]
print("Vetor original:", v)
resultado = selection_sort_decrescente(v)
print("Vetor em ordem decrescente:", resultado)
