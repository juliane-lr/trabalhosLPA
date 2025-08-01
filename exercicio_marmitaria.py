# Tamanho P de Bife Acebolado (BA) custa 16 reais e o Filé de Frango (FF) custa 15 reais;
# Tamanho M de Bife Acebolado (BA) custa 18 reais e o Filé de Frango (FF) custa 17 reais;
# Tamanho G de Bife Acebolado (BA) custa 22 reais e o Filé de Frango (FF) custa 21 reais;

# Início do Programa:
# Menu
print('#Bem-vindo à Marmitaria da Juliane Lopes da Rocha#')
print('<' * 20, 'CARDÁPIO', '>'*20)
print('-'*50)
print('Tamanho | Bife Acebolado (BA) | Filé de Frango (FF)')
print('-- P -- |      R$ 16.00       |       R$ 15.00    |')
print('-- M -- |      R$ 18.00       |       R$ 17.00    |')
print('-- G -- |      R$ 22.00       |       R$ 21.00    |')
print('-'*50)

# Início Acumulador
valorFinal = 0

while True:
    sabor = input('\nSelecione a opção desejada (BA/FF): ').upper()
    if sabor == 'BA' or sabor == 'FF':
        tamanho = input('Selecione o tamanho (P/M/G): ').upper()
        if sabor == 'BA':
            sabor_marmita = 'Bife Acebolado'
            if tamanho == 'P':
                valor = 16
            elif tamanho == 'M':
                valor = 18
            elif tamanho == 'G':
                valor = 22
            else:
                print('Tamanho inválido. Tente novamente.')
                continue
            valorFinal += valor
            print(f'Selecionado: {sabor_marmita}, tamanho {tamanho}. Valor = R$ {valor:.2f}.')
        
        else:
            sabor_marmita = 'Filé de Frango'
            if tamanho == 'P':
                valor = 15
            elif tamanho == 'M':
                valor = 17
            elif tamanho == 'G':
                valor = 21
            else:
                print('Tamanho inválido. Tente novamente.')
                continue
            valorFinal += valor
            print(f'Selecionado: {sabor_marmita}, tamanho {tamanho}. Valor = R$ {valor:.2f}.')
    else:
        print('Sabor inválido. Tente novamente.')
        continue

# Retornando ao laço:
    pedirMais = input('\nDeseja pedir mais alguma coisa? S/N ').upper()
    if pedirMais == 'S':
        continue
    else:
        break

print(f'\nFinalizando pedido. Valor total = R$ {valorFinal:.2f}')

    
       