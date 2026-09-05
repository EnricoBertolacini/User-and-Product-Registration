from models.produto import Produto


lista_produtos = []
def cadastrar_produto():
    id = int(input('ID:'))
    nome = input('NOME:')
    categoria = input('CATEGORIA:')
    preco = float(input('PREÇO:'))
    estoque = int(input('ESTOQUE:'))
    produto = Produto(id,nome,categoria,preco,estoque)
    lista_produtos.append(produto)
    print('Produto cadastrado')

def listar_produtos():
        if len(lista_produtos) == 0:
            print('Não existem produtos cadastrados no sistema')
        else:
            for p in lista_produtos:
                print(p)

def buscar_produto():
    id_busca = int(input('Digite o ID do produto que deseja buscar:'))
    encontrado = False
    for p in lista_produtos:
        if p.id == id_busca:
            print(p) 
            encontrado = True
            break
        
    if not encontrado:
        print('Produto não encontrado no sistema.')
    


def atualizar_produto():
    id_busca = int(input('Digite o ID do produto que deseja atualizar:'))
    encontrado = False
    for p in lista_produtos:
        if p.id == id_busca:
            print('---Atualização---')
            p.id = int(input('ID:'))
            p.nome = input('NOME:')
            p.categoria = input('CATEGORIA:')
            p.preco = float(input('PREÇO:'))
            p.estoque = int(input('ESTOQUE:'))
            print('Produto Atualizado')
            encontrado = True
            break

    if not encontrado:
        print('Produto não encontrado no sistema')
    
            

def remover_produto():
    id_busca = int(input('Digite o ID do produto que deseja remover:'))
    encontrado = False
    for p in lista_produtos:
        if p.id == id_busca:
            lista_produtos.remove(p)
            print('Produto removido')
            encontrado = True
    if not encontrado:
        print('Produto não encontrado no sistema')

    

def consultar_estoque():
    id_busca = int(input('Digite o ID do produto que deseja remover:'))
    encontrado = False
    for p in lista_produtos:
        if p.id == id_busca:
            print(f'{p.nome} : {p.estoque} unidades' )
            encontrado = True
    if not encontrado:
        print('Produto não encontrado no sistema')