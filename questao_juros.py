# qtd parcelas < 4 = juros 0%
# qtd parcelas >= 4 e < 6 = juros 4%
# qtd parcelas >= 6 e < 9 = juros 8%
# qtd parcelas >= 9 e < 13 = juros 16%
# qtd parcelas >= 13 = juros 32%

# Início do Programa:

print('|---Bem-vindo à loja da Juliane Lopes da Rocha!---|')
valorPedido = float(input('Digite o valor do pedido: '))
parcelas = int(input('Digite a quantidade de parcelas: '))

if parcelas < 4:
    valorParcela = (valorPedido*(1+0/100)/parcelas) # 0% de juros
elif parcelas < 6:
    valorParcela = (valorPedido*(1+4/100)/parcelas) # 4% de juros
elif parcelas < 9:
    valorParcela = (valorPedido*(1+8/100)/parcelas) # 8% de juros
elif parcelas < 13:
    valorParcela = (valorPedido*(1+16/100)/parcelas) # 16% de juros
else:
    valorParcela = (valorPedido*(1+32/100)/parcelas) # 32% de juros

print(f'\nValor da parcela = {valorParcela:.2f}.')
print(f'Valor total parcelado = {valorParcela * parcelas:.2f}.')