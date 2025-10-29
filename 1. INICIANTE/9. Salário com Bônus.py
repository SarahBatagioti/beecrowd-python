nome = str(input())
salarioFixo = float(input())
totalVenda = float(input())

totalComComissao = (0.15 * totalVenda) + salarioFixo 

print(f"TOTAL = R$ {totalComComissao:.2f}")

