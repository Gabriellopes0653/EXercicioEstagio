def maior_par_impar():
    #Recebe a entrada do usuário com números separados por espaços
    #O input é convertido para uma lista de inteiros usando map(int, ...)
    numeros = list(map(int, input("Digite os números separados por espaços: ").split()))

    #Cria uma lista de números pares a partir da lista de números
    pares = [num for num in numeros if num % 2 == 0]

    #Cria uma lista de números ímpares a partir da lista de números
    impares = [num for num in numeros if num % 2 != 0]

    #Se houver números pares, encontra o maior; caso contrário, retorna None
    maior_par = max(pares) if pares else None

    #Se houver números ímpares, encontra o maior; caso contrário, retorna None
    maior_impar = max(impares) if impares else None

    #Exibe o maior número par e o maior número ímpar (ou None se não houver)
    print(f'O maior par é {maior_par} e o maior ímpar é {maior_impar}')

#Chama a função para que o usuário possa inserir números e ver o resultado
maior_par_impar()
