# Dicionário de regras fonéticas
# Prioridade: dígrafos primeiro (sh, ch, etc.)
regras = {
    "shch": "щ",
    "zh": "ж",
    "ch": "ч",
    "sh": "ш",
    "ts": "ц",
    "yo": "ё",
    "yu": "ю",
    "ya": "я",
    "ye": "е",

    # letras simples
    "a": "а",
    "b": "б",
    "v": "в",
    "g": "г",
    "d": "д",
    "z": "з",
    "i": "и",
    "y": "й",
    "k": "к",
    "l": "л",
    "m": "м",
    "n": "н",
    "o": "о",
    "p": "п",
    "r": "р",
    "s": "с",
    "t": "т",
    "u": "у",
    "f": "ф",
    "h": "х"
}

#Função que translitera
def transliterar(palavra):

    resultado = []  # lista que armazenará os caracteres finais
    i = 0            # índice de leitura da palavra

    # percorre toda a palavra
    while i < len(palavra):
        match = None  # armazena a tradução encontrada

        # tenta casar primeiro os maiores padrões (até 4 letras)
        for tamanho in range(4, 0, -1):
            trecho = palavra[i:i + tamanho]

            # verifica se o trecho existe nas regras
            if trecho in regras:
                match = regras[trecho]
                i += tamanho  # avança no índice
                break

        # se encontrou regra, adiciona a tradução
        if match:
            resultado.append(match)
        else:
            # caso não exista regra, mantém o caractere original
            resultado.append(palavra[i])
            i += 1

    # junta tudo em uma única string
    return "".join(resultado)


# Entrada
palavra = input("Que palavra você deseja transliterar? ").lower()
#Cahamda da função que translitera a palavra
traduzida = transliterar(palavra)

print(f"A transliteração de {palavra} é: {traduzida}")
