carro = input("Qual carro deseja comprar: ")
estoque = ["BMW X6", "BMW i5", "BMW i8"]

if carro in estoque:
    print("O carro está disponível.")   
else:
    print("O carro não está disponível.")