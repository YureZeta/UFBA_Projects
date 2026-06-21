# Solicita ao usuário o peso em quilogramas (kg)
peso = float(input("Digite seu peso (kg): "))

# Solicita ao usuário a altura em metros (m)
altura = float(input("Digite sua altura (m): "))

# Calcula o IMC usando a fórmula: peso / (altura^2)
imc = peso / (altura ** 2)

# Exibe o resultado do IMC com 2 casas decimais
print(f"\nSeu IMC é: {imc:.2f}")

# Classificação de IMC

# Verifica em qual faixa o IMC se encaixa
if imc < 18.5:
    print("Classificação: Abaixo do peso")

# IMC entre 18.5 e 24.9
elif imc < 24.9:
    print("Classificação: Peso normal")

# IMC entre 25 e 29.9
elif imc < 29.9:
    print("Classificação: Sobrepeso")

# IMC entre 30 e 34.9
elif imc < 34.9:
    print("Classificação: Obesidade grau I")

# IMC entre 35 e 39.9
elif imc < 39.9:
    print("Classificação: Obesidade grau II")

# IMC maior ou igual a 40
else:
    print("Classificação: Obesidade grau III")