from services.cliente_service import cadastrar_cliente,listar_clientes,remover_cliente,buscar_cliente,atualizar_cliente

def menu_clientes():
    print('=' * 8 , 'PRODUTOS', '=' * 8)
    print('1-Cadastrar cliente')
    print('2-Listar clientes')
    print('3-Buscar cliente'  )
    print('4-Atualizar cliente')
    print('5-Remover cliente')
    print('0-Voltar')


def escolha_clientes():
    while True:
        menu_clientes()
        try:
            opcao = int(input('Digite uma opção:'))

            match opcao:
                case 1:
                    cadastrar_cliente()
                case 2:
                    listar_clientes()
                case 3:
                    buscar_cliente()
                case 4:
                    atualizar_cliente()
                case 5:
                    remover_cliente()
                case 0:
                    break
                case _:
                    print('Digite uma opção válida')
        except ValueError:
            print('Digite uma opção válida')