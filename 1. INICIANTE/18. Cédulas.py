valor = int(input())

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

    print(valor)
    print(f"{valor100} nota(s) de R$ 100,00")
    print(f"{valor50} nota(s) de R$ 50,00")
    print(f"{valor20} nota(s) de R$ 20,00")
    print(f"{valor10} nota(s) de R$ 10,00")
    print(f"{valor5} nota(s) de R$ 5,00")
    print(f"{valor2} nota(s) de R$ 2,00")
    print(f"{valor1} nota(s) de R$ 1,00")

else:
    print("Número inválido. Digite entre 1 e 999999")