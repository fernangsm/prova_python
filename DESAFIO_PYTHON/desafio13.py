numeros = [int(input("Digite o {i+1}º número: ")) for i in range(10)]
pares = [n for n in numeros if n % 2 == 0]
impares = [n for n in numeros if n % 2 != 0]
print("Pares:", pares)
print("Ímpares:", impares)