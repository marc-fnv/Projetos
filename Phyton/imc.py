altura = float(input("Qual sua altura (em metros): "))
peso = float(input("Qual o seu peso (em kg): "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print("Magreza")  
elif imc < 25:
    print("Normal")
elif imc < 30:
    print("Sobrepeso")        
elif imc < 40:
    print("Obesidade") 
else:    
    print("Obesidade grave")


first_name = input("Digite seu primeiro nome: ")
age = int(input("Digite sua idade: "))

print('Olá {}, você tem {} anos e seu IMC é {}'.format(first_name, age, imc))