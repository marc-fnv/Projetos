def calculo_fatorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * calculo_fatorial(numero - 1)

num = int(input("Digite um número para fatorial: "))
print(f"O fatorial de {num} é: {calculo_fatorial(num)}")