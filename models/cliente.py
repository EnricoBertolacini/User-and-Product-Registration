
class Cliente:
    def __init__ (self,nome,id,status):
        self.nome = nome
        self.id = id
        self.status = status

    def __repr__(self):
        return f'NOME:{self.nome} | ID:{self.id} | STATUS:{self.status} '

