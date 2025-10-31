infoPecas1 = str(input()).split()
infoPecas2 = str(input()).split()

codigoPeca1 = int(infoPecas1[0])
quantidadePeca1 = int(infoPecas1[1])
valorPeca1 = float(infoPecas1[2])

codigoPeca2 = int(infoPecas2[0])
quantidadePeca2 = int(infoPecas2[1])
valorPeca2 = float(infoPecas2[2])

totalAPagar = (valorPeca1 * quantidadePeca1) + (valorPeca2 * quantidadePeca2)
print(f"VALOR A PAGAR: R$ {totalAPagar:.2f}")