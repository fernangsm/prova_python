numeros = []
while True:
    entrada = input("Digite um número (ou 'sair' para encerrar): ")
    if entrada.lower() == 'sair':
        break
    num = int(entrada)
    if num % 5 == 0:
        numeros.append(num)
print("Soma dos múltiplos de 5:", sum(numeros))