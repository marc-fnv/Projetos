temperatura = int(input("Digite a temperatura da carne: "))

if temperatura < 48:
    print("Cozinhar por mais alguns minutos")  
elif temperatura in range(48, 53):
    print("Selada")
elif temperatura in range(54, 59):
    print("Ao ponto para o mal")        
elif temperatura in range(60, 64):
    print("Ao ponto") 
elif temperatura in range(65, 70):
    print("Ao ponto para o bem")
if temperatura >= 71:
    print("bem passada")
