class Televisão():

    def __init__(self,ano_tv,id_tv,marca_tv,preço_tv):

        self.ano_tv =ano_tv
        self.id_tv = id_tv
        self.marca_tv = marca_tv
        self.preco_tv = preço_tv
        self.__vendida = False

    
    def aumentar_preço(self,valor): 
        self.preco_tv += valor
        pass

    def diminiur_preço(self,valor):
        self.preco_tv -= valor
        pass

    def consultar(self):

        tv_dados = {"ID do aparelho":self.id_tv,"marca": self.marca_tv,"ano de fabricação":self.ano_tv,"preço":self.preco_tv}
        print(list(tv_dados.values()))
        print(list(tv_dados.keys()))



Tv = Televisão(2023,111,'sansung',1500)
print((Tv)) # saida = <__main__.Televisão object at 0x0000024F6A59DBD0> estes numeros e o endereço na memoria
#mas ao dar mais um print o espaço muda,pois o garbage collect muda automaticamente,porém
#<__main__.Televisão object at 0x0000022B8099DBD0>
#porém quando:
oi = Tv
print(oi)
#saida:<__main__.Televisão object at 0x0000022B8099DBD0> a locação fica na mesma
print(oi.marca_tv) #saida:sansung

#como acabr com este vinculo
'oi = None'
oi = None
print(oi)