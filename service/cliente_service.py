from models.cliente import Cliente


lista_clientes = []
def cadastrar_cliente():
    nome = input('NOME:').capitalize()
    id = int(input('ID:'))
    status = input('STATUS:')
    cliente = Cliente(nome,id,status)
    lista_clientes.append(cliente)
    print('Cliente cadastrado')

def listar_clientes():
    if len(lista_clientes) == 0:
        print('Nenhum cliente cadastrado no sistema')
    else:
        for c in lista_clientes:
            print(c)

def buscar_cliente():
    id = int(input('ID:'))
    encontrado = False
    for c in lista_clientes:
        if c.id == id:
            print(f'{c.nome} | {c.id} | {c.status}')
            encontrado = True
    if not encontrado:
        print('Cliente não encontrado no sistema.')

def atualizar_cliente():
    id = int(input('ID:'))
    encontrado = False
    for c in lista_clientes:
        if c.id == id:
            c.nome = input('NOME:')
            c.id = int(input('ID:'))
            c.status = input('STATUS:')
    if not encontrado:
        print('Cliente não encontrado no sistema.')


def remover_cliente():
    id = input('ID:')
    encontrado = False
    for c in lista_clientes:
        if c.id == id:
           lista_clientes.remove(c)
           print('Cliente removido com sucesso')
           encontrado = True
    if not encontrado:
        print('Cliente não encontrado no sistema.')