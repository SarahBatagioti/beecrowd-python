tempo = int(input())

x = tempo // 60
segundos = tempo % 60
minutos = x % 60
horas = x // 60

print(f"{horas:.0f}:{minutos:.0f}:{segundos:.0f}")


