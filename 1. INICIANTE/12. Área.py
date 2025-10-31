valores = str(input()).split()

A = float(valores[0])
B = float(valores[1])
C = float(valores[2])

triangulo = (A * C) / 2
circulo = 3.14159 * (C **2)
trapezio = ((A + B) * C) / 2
quadrado = B * B
retangulo = A * B

print(f"TRIANGULO: {triangulo:.3f}")
print(f"CIRCULO: {circulo:.3f}")
print(f"TRAPEZIO: {trapezio:.3f}")
print(f"QUADRADO: {quadrado:.3f}")
print(f"RETANGULO: {retangulo:.3f}")