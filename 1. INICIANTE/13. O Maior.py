valores = str(input()).split()

A = int(valores[0])
B = int(valores[1])
S = int(valores[2])

MaiorAB = (A + B + abs(A - B)) / 2
MaiorABeS = (MaiorAB + S + abs(MaiorAB - S)) / 2

print(f"{MaiorABeS:.0f} eh o maior")  