numero = int(input("Digite um numero:"))

soma = 0

while numero > 0:
    digito = numero % 10
    soma = soma + digito ** 2
    numero = numero // 10

    print(f"A soma dos dois digitos é:", soma)
