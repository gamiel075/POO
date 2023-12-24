import pandas as pd

class simular():

    #simulaçõ de operação

    def __init__(self,capacidade_estoque,qtd_armazenada):

        self.capacidade_estoque = capacidade_estoque
        self.qtd_armazenada = qtd_armazenada

    def processar(self):

        qtd_restante = self.capacidade_estoque - self.qtd_armazenada
        itens_avariados= float(input('qual é a quantidade de itens avariados'))
        itens_perdidos= float(input('qual é a quantidade de itens perdidos'))
        itens_lost = itens_avariados + itens_perdidos
        qtd_restante -= itens_lost

        dados = [                                                                            #vc pode passar essas informações em porcento
            ['armazenamento total',self.capacidade_estoque],                                # ou por exemplo colocar lost e dai o usuario clica para saber mais detalhes
            ['armazenamento',self.qtd_armazenada],                                          #lembra dos processos ddo meli, de que forma pode-se catalogar o estoque 
            ['itens lost',itens_lost]]
        
        df = pd.DataFrame(dados)
        print(df)

        def set_capacidade():
            pass 



     




        
