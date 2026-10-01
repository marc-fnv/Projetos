def calculo_potencia(base, expoente=2):
    resultado = base ** expoente
    print(f"O resultado da potência é: {resultado}")    

base = int(input("Digite a base: "))
expoente = input("Digite o expoente: ")

if expoente:
    calculo_potencia(base, int(expoente))
else: 
    calculo_potencia(base)