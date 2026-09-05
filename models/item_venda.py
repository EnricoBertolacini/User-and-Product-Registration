class ItemVenda:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade
        self.subtotal = produto.preco * quantidade

    def __repr__(self):
        return f'{self.produto} | {self.quantidade}'