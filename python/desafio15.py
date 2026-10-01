frutas = ["maçã","maçã","maçã", "banana", "laranja","morango"]

quantidade_macas = frutas.count("maçã")
print(f"Quantidade de maçãs: {quantidade_macas}")

qtd = 0
for fruta in frutas:
    if fruta == "maçã":
        qtd += 1
print(f"Quantidade de maçãs (usando loop): {qtd}")
