palavra = input("Digite a palavra soletrada em português (apenas em minúsculas): ").split() #Pede ao usuário que digite uma palavra nas línguas suportadas, sendo soletrada para facilitar os processos

letras = palavra   #Cria uma lista do mesmo tamannho e elementos para ser modificada

idioma = input("Digite o idioma que a frase deve ser traduzida: ") #Pede ao usuário que digite o idioma ao qual se deve traduzir a palavra

#Listas que impedem confusões de digitação
RussianNames = ["Russo", "russo", "RUSSO"]
BrasilianNames = ["Português", "português", "Portugues", "PORTUGÊS"]

#Alfabetos em listas
russo = []
brasileiro = ["a", 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#Função que identifica a correspondência de cada letra
def mapeia_letra(caracter):
    c = caracter
    if idioma in BrasilianNames:
        for letra in range(26):
            if brasileiro[letra] == c:
                return letra
                break




#Função que trata as correspondências e gera a plavra traduzida para um idioma selecionado
def traduzir(letrasT):
    alfabeto = letrasT
    traducao = []
    if idioma in BrasilianNames:
        for i in alfabeto:
            traducao.append(brasileiro[i])
    return traducao

#Lista que recebe as letras da palavra
letrasT = []

for i in range(len(letras)):
      caracter = letras[i]
      letrasT.append(mapeia_letra(caracter))

palavraT = traduzir(letrasT)
palavraT = .split()palavraT
print("A palavra digitada foi: ", *palavra)
print(f"Sua tradução em {idioma} é:", *palavraT)
