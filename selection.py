def selectionsort(vetor): 
    
    tamanho = len(vetor)
    for i in range (tamanho - 1 ):
        min = i
        for j in range (i+1, tamanho):
            if vetor[j] < vetor[min]:
                min = j
        if min != i:
            vetor[i], vetor[min] = vetor[min], vetor[i]
        print(vetor)  
      
       
            
vetor= []
for i in range(0,4):
    vetor.append(int (input ('digite um número')))

print(vetor)

selectionsort(vetor)


