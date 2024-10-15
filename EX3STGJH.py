def sao_anagramas():
    #Recebe a primeira string do usuário
    string1 = input("Digite a primeira palavra ou frase: ")

    #Recebe a segunda string do usuário
    string2 = input("Digite a segunda palavra ou frase: ")

    #Remove os espaços e converte as strings para letras minúsculas
    string1 = string1.replace(" ", "").lower()
    string2 = string2.replace(" ", "").lower()

    #Verifica se as duas strings têm o mesmo tamanho após o tratamento
    #Se o tamanho for diferente, não podem ser anagramas
    if len(string1) != len(string2):
        print("Não são anagramas")
        return  #Encerra a função se o tamanho for diferente

    #Ordena as letras de ambas as strings e compara
    #Se as strings ordenadas forem iguais, são anagramas
    if sorted(string1) == sorted(string2):
        print("São anagramas")
    else:
        #Se as strings ordenadas forem diferentes, não são anagramas
        print("Não são anagramas")

#Chama a função para o usuário testar se duas strings são anagramas
sao_anagramas()
