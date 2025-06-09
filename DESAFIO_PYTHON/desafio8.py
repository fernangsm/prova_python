frase = input("Digite uma frase: ").lower()
vogais = sum(1 for c in frase if c in "aeiou")
print("Total de vogais:", vogais)