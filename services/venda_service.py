from services.cliente_service import lista_clientes
from services.produto_service import lista_produtos
from models.item_venda import ItemVenda
from models.venda import Venda




def verificar_cliente():
    id_cliente = int(input('ID CLIENTE:'))

    for cliente in lista_clientes:
        if cliente.id == id_cliente:
            print('NOVA VENDA')
            print(f'Cliente: {cliente.nome}')
            return cliente

    print('Cliente não encontrado no sistema.')
    return None

lista_vendas = []
def fazer_venda():
    cliente = verificar_cliente()
    if cliente is None:
        return None
    
    if len(lista_vendas) == 0:
        id_venda = 1
    else:
        maior_id = 0
        for venda in lista_vendas:
            if venda.id_venda > maior_id:
                maior_id = venda.id_venda
        id_venda = maior_id + 1
    print(f'Venda #{id_venda}')
    venda = Venda(cliente,id_venda)
    return venda

def adicionar_produtos(venda):
    while True:
        id_produto = int(input('ID PRODUTO:'))
        encontrado = False

        for produto in lista_produtos:
            if produto.id == id_produto:
                print(f'Produto: {produto.nome}')

                quantidade = int(input('Digite a quantidade:'))

                item_existente = None

            
                for item in venda.itens:
                    if item.produto.id == id_produto:
                        item_existente = item
                        break

                
                if item_existente:
                    quantidade_total = item_existente.quantidade + quantidade

                    if quantidade_total <= produto.estoque:
                        item_existente.quantidade = quantidade_total
                    else:
                        print('Estoque indisponível')

                
                else:
                    if quantidade <= produto.estoque:
                        item = ItemVenda(produto, quantidade)
                        venda.itens.append(item)
                    else:
                        print('Estoque indisponível')

                encontrado = True

        if not encontrado:
            print('Produto não encontrado no sistema')

        resposta = input('Adicionar mais itens (S/N)?').capitalize()

        if resposta != 'S':
            break
def remover_produto(venda):
     id = int(input('ID:'))
     encontrado = False
     for item in venda.itens:
          if item.produto.id == id:
               venda.itens.remove(item)
               print(f'{item.produto.nome} foi removido!')
               encontrado = True
     if not encontrado:
        print('Produto não encontrado na lista')
               
def calcular_total(venda):
    total = 0
    for item in venda.itens:
          total += item.subtotal
    return total

          
def resumo_pedido(venda):
    print(20*'-')
    for item in venda.itens:
       print(f'{item.quantidade}x {item.produto.nome} {item.produto.preco}')
    print(20*'-')
    total = calcular_total(venda)
    print(f'TOTAL: {total}')




def finalizar_pedido(venda):
    resposta = input('Deseja finalizar a venda?(S/N)').capitalize()
    if resposta == 'S':
        for item in venda.itens:
            item.produto.estoque -= item.quantidade
        print('Venda finalizada!')
        print(30*'-')
        print('Resumo da venda')
        resumo_pedido(venda)
        lista_vendas.append(venda)
        return True

    
    print('Venda não confirmada!')
    return False
    


def mostrar_venda():
    if len(lista_vendas) == 0:
                print('Nenhuma venda registrada')
    for venda in lista_vendas:
        pass
        id = venda.id_venda
        cliente = venda.cliente.nome
        for item in venda.itens:
            produto = item.produto.nome
            quantidade = item.quantidade
            total = item.subtotal
            print(f'ID VENDA:{id} | CLIENTE:{cliente} | PRODUTO:{produto} | QUANTIDADE:{quantidade} | TOTAL:{total}')
               


def relatorio_vendas():
    print('================ RELATÓRIO DE VENDAS ================')

    faturamento_total = 0
    produtos_vendidos = 0
    total_vendas = len(lista_vendas)

    vendas_por_produto = {}

    for venda in lista_vendas:
        for item in venda.itens:
            faturamento_total += item.subtotal
            produtos_vendidos += item.quantidade

            if item.produto.nome in vendas_por_produto:
                vendas_por_produto[item.produto.nome] += item.quantidade
            else:
                vendas_por_produto[item.produto.nome] = item.quantidade

    if total_vendas > 0:
        ticket_medio = faturamento_total / total_vendas
    else:
        ticket_medio = 0

    if vendas_por_produto:
        produto_mais_vendido = max(
            vendas_por_produto,
            key=vendas_por_produto.get
        )
    else:
        produto_mais_vendido = 'Nenhum'

    print(f'Total de vendas: {total_vendas}')
    print(f'Faturamento total: R${faturamento_total:.2f}')
    print(f'Produtos vendidos: {produtos_vendidos} unidades')
    print(f'Ticket Médio: R${ticket_medio:.2f}')
    print(f'Produto mais vendido: {produto_mais_vendido}')




