meuPrimo = int(input("verifique se seu número é primo: "))

i = 1
divisorTotal = 0
primosTotais = []

while i < meuPrimo:
    checarPrimo = meuPrimo/i
    if f'{checarPrimo:.9f}'[2:5] == '0':
        divisorTotal += 1
        i += 1
    else:
        primosTotais.append(i)
        i += 1
    
if divisorTotal > 2:
    print(meuPrimo, "não é um número primo")
else:
    print(meuPrimo, "é um número primo")
