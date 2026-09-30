def funcao_dobro_valor(valor):
    return valor * 2

def funcao_quadrado_valor(valor):
    return valor ** 2

numero = int(input("Digite um número: "))
resultado = funcao_quadrado_valor(funcao_dobro_valor(numero))
print(f"O resultado do dobro do número ao quadrado é: {resultado}")
