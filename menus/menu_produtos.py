from services.produto_service import cadastrar_produto,listar_produtos,remover_produto,buscar_produto,atualizar_produto,consultar_estoque
def menu_produtos():
    print('=' * 8 , 'PRODUTOS', '=' * 8)
    print('1-Cadastrar produto')
    print('2-Listar produtos')
    print('3-Buscar produto')
    print('4-Atualizar produto')
    print('5-Remover produto')
    print('6-Consultar estoque')
    print('0-Voltar')
    

def escolha_produtos():
    while True:
        menu_produtos()
        try:
            opcao = int(input('Digite uma opção:'))

            match opcao:
                case 1:
                    cadastrar_produto()
                case 2:
                    listar_produtos()
                case 3:
                    buscar_produto()
                case 4:
                    atualizar_produto()
                case 5:
                    remover_produto()
                case 6:
                    consultar_estoque()
                case 0:
                    break
                case _:
                    print('Digite uma opção válida')
        except ValueError:
            print('Digite uma opção válida')

#FIM MENU PRODUTOS