x1y1 = str(input()).split()
x2y2 = str(input()).split()

x1 = float(x1y1[0])
y1 = float(x1y1[1])

x2 = float(x2y2[0])
y2 = float(x2y2[1])

distancia = ((x2-x1)**2 + (y2-y1)**2)**0.5

print(f"{distancia:.4f}")


