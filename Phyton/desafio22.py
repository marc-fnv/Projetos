capital =  {
        "Brasil": "Brasília",
        "Argentina": "Buenos Aires",
        "Chile": "Santiago",
        "Austrália": "Canberra",
        "Canadá": "Ottawa" }

pais = input("Digite o nome do país: ")

if pais in capital:
    print(f"A capital do {pais} é {capital[pais]}.")
else:
    print("País não encontrado.")    