valor = float(input())

if valor > 0 and valor < 1000000:
    valor100 = valor // 100
    calc50 = valor - valor100 * 100
    
    valor50 = calc50 // 50 
    calc20 = calc50  - valor50 * 50 
    
    valor20 = calc20 // 20
    calc10 = calc20 - valor20 * 20 
    
    valor10 = calc10 // 10
    calc5 = calc10 - valor10 * 10 
    
    valor5 = calc5 // 5
    calc2 = calc5 - valor5 * 5
    
    valor2 = calc2 // 2
    calc1 = calc2 - valor2 * 2 
    
    valor1 = calc1 // 1
    calc050 = calc1 - valor1 * 1
    
    valor050 = calc050 // 0.50
    calc025 = calc050 - valor050 * 0.50
    
    valor025 = calc025 // 0.25
    calc010 = calc025 - valor025 * 0.25
    
    valor010 = calc010 // 0.10
    calc005 = calc010 - valor010 * 0.10
    
    valor005 = calc005 // 0.05
    calc001 = calc005 - valor005 * 0.05
    
    valor001 = round(calc001 / 0.01) 
    
    print("NOTAS:")
    print(f"{valor100:.0f} nota(s) de R$ 100.00")
    print(f"{valor50:.0f} nota(s) de R$ 50.00")
    print(f"{valor20:.0f} nota(s) de R$ 20.00")
    print(f"{valor10:.0f} nota(s) de R$ 10.00")
    print(f"{valor5:.0f} nota(s) de R$ 5.00")
    print(f"{valor2:.0f} nota(s) de R$ 2.00")
    print("MOEDAS:")
    print(f"{valor1:.0f} moeda(s) de R$ 1.00")
    print(f"{valor050:.0f} moeda(s) de R$ 0.50")
    print(f"{valor025:.0f} moeda(s) de R$ 0.25")
    print(f"{valor010:.0f} moeda(s) de R$ 0.10")
    print(f"{valor005:.0f} moeda(s) de R$ 0.05")
    print(f"{valor001:.0f} moeda(s) de R$ 0.01")
else:
    print("Número inválido. Digite entre 1 e 999999")