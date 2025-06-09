numero = int(input("Digite um número para ver a tabuada: "))

print("\nTabuada de multiplicação do {numero}:\n")

for i in range(1, 11):
    resultado = numero * i
    print("{numero} x {i:2} = {resultado}")
