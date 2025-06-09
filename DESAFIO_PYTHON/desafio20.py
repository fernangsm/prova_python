a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
op = input("Escolha a operação (soma, subtracao, multiplicacao, divisao): ").lower()

if op == 'soma':
    print("Resultado:", a + b)
elif op == 'subtracao':
    print("Resultado:", a - b)
elif op == 'multiplicacao':
    print("Resultado:", a * b)
elif op == 'divisao':
    print("Resultado:", a / b if b != 0 else "Erro: divisão por zero")
else:
    print("Operação inválida.")