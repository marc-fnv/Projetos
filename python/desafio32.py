numeros = [1, 2, 3, 4, 5, 6]
quadrado = lambda numero: numero ** 2

lista_resultado = []

for numero in numeros:
    lista_resultado.append(quadrado(numero))

print('Os quadrados dos números', numeros, 'são:', lista_resultado)    