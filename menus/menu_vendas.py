from services.venda_service import verificar_cliente,adicionar_produtos,calcular_total,resumo_pedido,remover_produto,finalizar_pedido,fazer_venda
def menu_vendas():
    print('1-Adicionar produto')
    print('2-Remover produto')
    print('3-Ver venda')
    print('4-Finalizar')
    print('0-Cancelar')



def escolha_menu_vendas():
    venda = fazer_venda()
    if venda is None:
        return
    while True:
        menu_vendas()
        opcao = int(input('Digite uma opção:'))
        match opcao :
            case 1:
                adicionar_produtos(venda)
            case 2:
                remover_produto(venda)
            case 3:
                resumo_pedido(venda)
            case 4:
                finalizada = finalizar_pedido(venda)
                if finalizada:
                    break
            case 0:
                print('Venda Cancelada!')
                break