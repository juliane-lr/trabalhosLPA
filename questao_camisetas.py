# Camiseta Manga Curta Simples (MCS) R$ 1,80 
# Camiseta Manga Longa Simples (MLS) R$ 2,10 
# Camiseta Manga Curta Com Estampa (MCE) R$ 2,90 
# Camiseta Manga Longa Com Estampa (MLE) R$ 3,20

# < 20 - não há desconto
# >=20 e <200 - desconto de 5%
# # >= 200 e < 2000 - desconto de 7%
# >=  2000 e <= 20000 - desconto de 12%
# > 20000 - não é aceito pedidos nessa quantidade de camisetas

# Frete por transportadora (1) - R$ 100
# Frete por Sedex (2) - R$ 200
# Retirar o pedido na fábrica (0)- R$ 0

# total = (modelo * num_camisetas) + frete

# Função Escolha Modelo:
def escolha_modelo():
    while True:
        print('Digite o modelo desejado: ')
        print('MCS - Camiseta Manga Curta Simples')
        print('MLS - Camiseta Manga Longa Simples')
        print('MCE - Camiseta Manga Curta Com Estampa')
        print('MLE - Camiseta Manga Longa Com Estampa')
        modelo = input('>> ').upper()
        if modelo == 'MCS':
            return 1.80
        elif modelo == 'MLS':
            return 2.10
        elif modelo == 'MCE':
            return 2.90
        elif modelo == 'MLE':
            return 3.20
        else:
            print('Opção inválida, tente novamente.\n')
            continue

# Função Número de Camisetas:
def num_camisetas():
    while True:
        try:
            qtd = int(input('Digite o número de camisetas: '))
            if qtd < 20:
                return qtd
            elif qtd < 200:
                return qtd*0.95
            elif qtd < 2000:
                return qtd*0.93
            elif qtd <= 20000:
                return qtd*0.88
            else:
                print('Nosso limite é de 20.000 camisetas por pedido. \nDigite outro valor.\n')
                continue
        except:
            print('Valor não numérico, tente novamente.\n')
            continue
            
# Função Frete:
def frete():
    while True:
        print('Escolha o tipo de frete: ')
        print('1 - Frete por transportadora = R$ 100,00')
        print('2 - Frete por Sedex = R$ 200,00')
        print('0 - Retirada na fábrica = R$ 0,00')
        add_frete = int(input('Digite a opção desejada: 0/1/2: '))
        if add_frete == 1:
            return 100
        elif add_frete == 2:
            return 200
        elif add_frete == 0:
            return 0
        else:
            print('Opção inválida, tente novamente.\n')


# Início do Programa:

print('=' * 50)
print('Bem-vindo à Camisetaria da Juliane Lopes da Rocha!')
print('=' * 50)
print()
valor_modelo = escolha_modelo() # Define o valor do modelo
print()
qtd_camisetas = num_camisetas() # Define a quantidade
print()
valor_frete = frete() # Define o frete

valor_total = valor_modelo * qtd_camisetas + valor_frete
print()
print(f'Valor total = R$ {valor_total:.2f}. (Valor do modelo: {valor_modelo:.2f} * Quantidade (com desconto): {qtd_camisetas:.2f}) + frete: R$ {valor_frete:.2f}.')

