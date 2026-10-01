par_impar = lambda num: "par" if num % 2 == 0 else "ímpar"

numero = int(input("Digite um número: "))
resultado = par_impar(numero)
print(f"O número {numero} é {resultado}.")