def bubblesort(vetor): 
    tamanho = len(vetor)
    for i in range (tamanho):
        for j in range (tamanho -1): 
            if vetor[j]> vetor[j+1]:   
                vetor[j], vetor[j+1] = vetor[j+1], vetor[j]
                print(vetor)

vetor= []
for i in range(0,4):
    vetor.append(int (input ('digite um número')))

print(vetor)

bubblesort(vetor)