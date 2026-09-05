class Produto:
    def __init__(self,id,nome,categoria,preco,estoque):
        self.id = id
        self.nome = nome
        self.categoria = categoria
        self.preco = preco
        self.estoque = estoque

    def __repr__(self):
        return f'ID:{self.id} | NOME:{self.nome} | CATEGORIA:{self.categoria} | PREÇO {self.preco}| ESTOQUE: {self.estoque}'



    




