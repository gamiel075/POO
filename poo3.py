class Televisão():

    def __init__(self,ano_tv,id_tv,marca_tv,preço_tv):

        self.id_tv = id_tv
        self.ano_tv =ano_tv
        self.marca_tv = marca_tv
        self.preco_tv = preço_tv
        self.__private = False #o andescor antes da a entender que ela é privada ou seja, sem alteração,variavel não aberta
        #a partir desta alteração muitas coisas podem ser feitas , especialmente em contas bancarias.



    
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




tv1 = Televisão(1114665,2023,'lg',1500)

#saida = [2023, 'lg', 1114665, 1500]
#['ID do aparelho', 'marca', 'ano de fabricação', 'preço']
print(type(tv1.__private)) #saida = False







print(tv1.__status_privado)


    
 
 
    
        