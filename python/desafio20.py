# numero = [1, 2, 3, 4, 5,6, 7, 8, 9, 10]

numero = list(range(1, 11))

Valor = int(input("Digite um número: "))


for Valor in numero:
    if Valor % 2 == 0:
        print(f"{Valor} é par.")
    else:
        print(f"{Valor} é ímpar.")
   