def calcular_fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calcular_fatorial(n - 1)

numero = int(input("Digite um número inteiro para calcular o fatorial: "))

if numero < 0:
    print("Fatorial não está definido para números negativos.")
else:
    resultado = calcular_fatorial(numero)
    print("O fatorial de {numero} é {resultado}")