# def multiplicar(num1, num2):
#     return num1 * num2

multiplicar = lambda num1, num2: num1 * num2

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

resultado_multiplicacao = multiplicar(numero1, numero2)

print(f"O resultado da multiplicação dos números {numero1} e {numero2} é: {resultado_multiplicacao}")