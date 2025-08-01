# Função de cadastro:
def cadastrar_funcionario(id):
    print('\nCADASTRAR FUNCIONÁRIO:')
    nome = input('Digite o nome do funcionário: ')
    setor = input('Digite o setor do funcionário: ')
    salario = float(input('Digite o salário do funcionário: '))
    funcionario = {'id':id, 'nome':nome, 'setor':setor, 'salario':salario} 
    lista_funcionarios.append(funcionario.copy())
    print()
    
# Função de consulta:
def consultar_funcionarios():
    while True:
        print('\nCONSULTAR FUNCIONÁRIOS:')
        print('1 - Consultar Todos')
        print('2 - Consultar por Id')
        print('3 - Consultar por Setor')
        print('4 - Retornar ao Menu')
        opcao = input('Digite a opção desejada: ')
        print()
        if opcao == '1': # Consulta todos
            for funcionario in lista_funcionarios:
                for chave, valor in funcionario.items():
                    print(f'{chave}: {valor}') 
                print('-' * 25)

        elif opcao == '2': # Consulta por id
            consultaid = int(input('Digite o Id: '))
            print()
            for funcionario in lista_funcionarios:
                if funcionario['id'] == consultaid:
                    for chave, valor in funcionario.items():
                        print(f'{chave}: {valor}')
                    print('-' * 25)
                            
        elif opcao == '3': # Consulta por setor
            consultasetor = input('Digite o Setor: ')
            print()
            for funcionario in lista_funcionarios:
                if funcionario['setor'] == consultasetor:
                    for chave, valor in funcionario.items():
                        print(f'{chave}: {valor}')
                    print('-' * 25)
                    
        elif opcao == '4':
            print()
            return
        
        else:
            print('Opção inválida. Tente novamente.')
            continue

# Função de remoção:
def remover_funcionario():
    while True:
        idremove = int(input('Digite o id do funcionário a ser removido: '))
        for funcionario in lista_funcionarios:
            if funcionario['id'] == idremove:
                lista_funcionarios.remove(funcionario)
                print(f'{funcionario} removido com sucesso.')
                print('\nRetornando ao Menu Principal.\n')
                return
    
        print('Id inválido. Funcionário não localizado no sistema. Confirme se o id está correto e tente novamente.')
        continue   
            


# Início do Programa:
lista_funcionarios = []
id_global = 5356355 

print('Bem-vindo à empresa da Juliane Lopes da Rocha')
print('-' * 45)

while True:
    print('-' * 14, 'MENU PRINCIPAL', '-' * 14)
    print('-' * 45)
    print('1 - Cadastrar Funcionário')
    print('2 - Consultar Funcionário')
    print('3 - Remover Funcionário')
    print('4 - Encerrar Programa')
    selecao = input('Selecione a opção desejada: ')
    if selecao == '1':
        cadastrar_funcionario(id_global)
        id_global += 1

    elif selecao == '2':
        consultar_funcionarios()

    elif selecao == '3':
        remover_funcionario()

    elif selecao == '4':
        print('Encerrando o programa.')
        break
    else:
        continue

