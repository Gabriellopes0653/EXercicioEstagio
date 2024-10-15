def contar_vogais_usuario():
    #Define uma string contendo todas as vogais, incluindo vogais acentuadas
    vogais = 'aáàâãeéêiíoóôõuú'

    #Inicializa o total de vogais para acumular a soma de todas as frases
    total_vogais = 0

    #Laço infinito que vai pedir repetidamente frases ao usuário
    while True:

        #Solicita ao usuário que digite uma frase e converte para minúsculas
        frase = input("Digite uma palavra ou uma frase: ").lower()

        #Se a frase for uma string vazia, o laço para
        if frase == '':
            break

        #Inicializa o contador de vogais para a frase atual
        contador = 0

        #Itera sobre cada caractere da frase digitada
        for caractere in frase:

            #Se o caractere for uma vogal (incluindo as acentuadas), incrementa o contador
            if caractere in vogais:
                contador += 1

        #Soma o numero de vogais da frase atual ao total de todas as frases
        total_vogais += contador

        #Exibe o numero de vogais encontradas na frase atual
        print(f'Frase: "{frase}" tem {contador} vogais.')

    #Após o laço ser cencerrado, exibe o total de vogais encontradas em todas as frases digitadas
    print(f'Total de vogais em todas as frases: {total_vogais}')

#Chama a função para iniciar a contagem de vogais com interação do usuário
contar_vogais_usuario()
