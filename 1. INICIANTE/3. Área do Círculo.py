n = 3.14159
raio = float(input())
area = n * raio ** 2
print(f"A={area:.4f}")

# print(f"A={round(area,4)}")
# round() arredonda o valor numérico, mas quando você imprime um float, o Python não mostra zeros à direita “inúteis”.