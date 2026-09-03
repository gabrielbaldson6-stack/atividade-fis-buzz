# Lista de compras

itens = []
total = 0

quantidade = int(input("Quantos itens você deseja adicionar? "))

for i in range(quantidade):
    nome = input(f"\nDigite o nome do item {i + 1}: ")
    preco = float(input(f"Digite o preço de {nome}: R$ "))

    itens.append((nome, preco))
    total += preco

print("\n===== RESUMO DA COMPRA =====")

for item, preco in itens:
    print(f"{item}: R$ {preco:.2f}")

print("----------------------------")
print(f"Total: R$ {total:.2f}")
