def selection_sort_k_trocas(A, k):
    n = len(A)
    trocas = 0  # contador de trocas realizadas
    
    for i in range(n):
        # encontra o índice do menor elemento a partir de i
        min_idx = i
        for j in range(i+1, n):
            if A[j] < A[min_idx]:
                min_idx = j
        
        # realiza a troca se necessário
        if min_idx != i:
            A[i], A[min_idx] = A[min_idx], A[i]
            trocas += 1
        
        # verifica se já realizamos k trocas
        if trocas == k:
            break
    
    return A

# Exemplo de uso
vetor = [5, 3, 4, 1, 2]
k = 2
resultado = selection_sort_k_trocas(vetor, k)
print(resultado)
