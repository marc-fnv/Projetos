idade = int(input("Digite sua idade: "))
if idade < 13:  
    print("Você é um criança.")
elif idade in range(13, 18):
    print("Você é um adolescente.")
else:
    print("Você é um adulto.")