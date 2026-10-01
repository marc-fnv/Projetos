# def cubo(numero):
#     return numero ** 3

# num = int(input("Digite um número: "))
# resultado = cubo(num)
# print(f"O cubo de {num} é: {resultado}")

cubo = lambda numero: numero ** 3

num = int(input("Digite um número: "))
resultado = cubo(num)
print(f"O cubo de {num} é: {resultado}")