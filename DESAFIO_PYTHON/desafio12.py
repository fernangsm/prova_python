texto = input("Digite um texto: ")
quantidade_letras = 0
for caractere in texto:
    if caractere.isalpha():
     quantidade_letras += 1
print("O texto tem {quantidade_letras} letras.")