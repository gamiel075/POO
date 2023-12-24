class Televisão():

    def __init__(self,ano_tv,id_tv,marca_tv,preço_tv):

        self.id_tv = id_tv
        self.ano_tv =ano_tv
        self.marca_tv = marca_tv
        self.preco_tv = preço_tv
        self._private = False 

    @property
    def marca(self):
        return self._marca_tv
    
    @marca.setter
    def marca(self,nova_marca):
        self._marca_tv = nova_marca

    
    def aumentar_preço(self,valor): 
        self.preco_tv += valor
        pass

    def diminiur_preço(self,valor):
        self.preco_tv -= valor
        pass

    def consultar(self):

        tv_dados = {"ID do aparelho":self.id_tv,"marca": self.marca_tv,"ano de fabricação":self.ano_tv,"preço":self.preco_tv}
        print(tv_dados)
        'print(list(tv_dados.values()))'
        'print(list(tv_dados.keys()))'

tv1 = Televisão('2023',555,'sansung',1500)
tv1.marca_tv = 'lg'
tv1.consultar() 