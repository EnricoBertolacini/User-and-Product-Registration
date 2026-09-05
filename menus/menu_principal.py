from menus.menu_produtos import escolha_produtos
from menus.menu_clientes import escolha_clientes
from menus.menu_vendas import escolha_menu_vendas
from services.venda_service import mostrar_venda,relatorio_vendas

def vermenu_principal():
    
    print('=' * 50)
    print('         SISTEMA DE ESTOQUE E VENDAS   ')
    print('=' * 50)
    print('1-Produtos')
    print('2-Clientes')
    print('3-Realizar Vendas')
    print('4-Histórico de Vendas')
    print('5-Relatórios')
    print('0-Sair')
    

  
def escolha_opcao_menu_principal():
    while True:
        vermenu_principal()
        try:
            opcao = int(input('Digite uma opção:'))

            match opcao:
                case 1:
                    escolha_produtos()
                case 2:
                    escolha_clientes()
                case 3:
                    escolha_menu_vendas()
                case 4:
                    mostrar_venda()
                case 5:
                    relatorio_vendas()
                case 0:
                    break
                case _:
                    print('Digite uma opção válida')
        except ValueError:
            print('Digite uma opção válida')

# FIM MENU PRINCIPAL