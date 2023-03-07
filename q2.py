num = int(input("Digite um número: "))

fibonacci = [0, 1]
while fibonacci[-1] < num:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

if num in fibonacci:
    print("O número", num, "pertence à sequência de Fibonacci.")
else:
    print("O número", num, "não pertence à sequência de Fibonacci.")
