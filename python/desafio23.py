# sets
amigos1 = {"Carlos", "Ana", "João", "Maria", "Pedro"}
amigos2 = {"Ana", "João", "Lucas", "Fernanda", "Mariana"}

# Interseção - amigos em comum
amigos_em_comum = amigos1.intersection(amigos2)

# OU amigos_em_comum = amigos1 & amigos2 

amigos_uniao = amigos1.union(amigos2)
amigos_diferenca = amigos1.difference(amigos2)

print(f"Amigos em comum: {amigos_em_comum}")
print(f"Amigos na união: {amigos_uniao}")
print(f"Amigos na diferença: {amigos_diferenca}")