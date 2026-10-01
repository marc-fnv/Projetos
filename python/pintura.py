rendimento_lata = int(input("Qual o rendimento da lata de tinta (em metros quadrados): "))
altura_parede = int(input("Qual a altura da parede (em metros): "))
largura_parede = int(input("Qual a largura da parede (em metros): "))


def calcular_latas_necessarias():
   metros_parede = altura_parede * largura_parede
   latas_necessarias = metros_parede / rendimento_lata
   print(f"Você precisará de {latas_necessarias} latas de tinta.")

calcular_latas_necessarias()   