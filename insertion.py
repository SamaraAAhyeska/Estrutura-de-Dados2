def insertionsort(vetor): 
    tamanho = len(vetor)
    for i in range (1, tamanho):
        valor = vetor[i]
        j = i - 1
        while j >=0 and vetor[j]> valor :
            vetor[j+1] = vetor[j]  
            j -=1 
        vetor[j+1] = valor
        print(vetor)

            
vetor= []
for i in range(0,4):
    vetor.append(int (input ('digite um número')))

print(vetor)

insertionsort(vetor)