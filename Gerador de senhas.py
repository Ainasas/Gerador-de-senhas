import random

caracteres = "ABCDEFGHIJKLMNOPQRSTUVXWYZabcdefghijklmnopqrstuvxwyz1234567890!@#$%¨&*()_-+?|/"

print("---Iniciando gerador de senhas---")

tamanho = int(input("Qual o tamanho da(s) senha(s) que você quer gerar? "))

quantidade = int(input("Quantas senhas você quer gerar? "))

print("\nAqui estão suas senhas!")

for quant in range(quantidade):
    senha = ""
    for senhas in range(tamanho):
        senha += random.choice(caracteres)
    print(senha)

print("Fim do gerador de senhas, obrigado por usar!")