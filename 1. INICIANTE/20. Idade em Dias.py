idadeEmDias = int(input())

quantAnos = idadeEmDias // 365
calcMes = idadeEmDias % 365

quantMeses = calcMes // 30
quantDias = calcMes % 30

print(f"{quantAnos} ano(s)")
print(f"{quantMeses} mes(es)")
print(f"{quantDias} dia(s)")
