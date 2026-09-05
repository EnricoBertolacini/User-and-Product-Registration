class Venda:
    def __init__(self,cliente,id_venda):
        self.cliente = cliente
        self.itens = []
        self.id_venda = id_venda

    def __repr__ (self):
        return f'{self.cliente.nome} | {self.itens} {self.id_venda}'