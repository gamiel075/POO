import abc

class totem_armazenamento(abc.ABC):
    
    def __init__(self,id,qtd_produtos,tipo):
        self.id = id
        self.qtd_produtos =  qtd_produtos
        self.tipo = tipo

    @abc.abstractclassmethod
    def romaneio(self):

        print(self.id)
        print(self.qtd_produtos)
        print(self.tipo)


class mono (totem_armazenamento):

     def romaneio(self):

        print(self.id)
        print(self.qtd_produtos)
        print(self.tipo)


a = mono(111,20,'tipo a')
print(a.id) #saida: 111 








    



