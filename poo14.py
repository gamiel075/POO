class Encomenda:

    def __init__(self,id,nome_destinátario,mês_expedição,valor):
        self.id = id
        self._nome_destinátario = nome_destinátario
        self.mês_expedição = mês_expedição
        self._valor = valor

    def taxa(self):
        return self._valor * 0.5 
    

class Carro(Encomenda):
    def  __init__(self,id,nome_destinátario,mês_expedição,valor,modelo,ano,taxa_envio):
        super().__init__(id,nome_destinátario,mês_expedição,valor)
        self.modelo =  modelo
        self.ano = ano
        self.taxa_envio = taxa_envio

    def taxa(self):
        return self._valor * 0.5 


class Peças(Encomenda):

    def  __init__(self,id,nome_destinátario,mês_expedição,valor,nome_peça,modelo,estado):
        super().__init__(id,nome_destinátario,mês_expedição,valor)
        self.nome_peça = nome_peça
        self.modelo = modelo
        self.estado = estado

    
    def taxa(self):

        taxa = 0

        if(self.estado == 'Novo'):
            taxa += 0.8
        elif(self.estado == 'Semi-Novo'):
            taxa += 0.6

        elif(self.estado == 'Usado'):
            taxa += 0.4
        elif(self.estado == 'Recondicionado'):
            taxa += 0.2

        v1 = self._valor * 0.5 * taxa
        self._valor += v1 
        return self._valor
 
     

carro_1 = Carro(101, 'Rafael', 'Maio', 18000, 'Fusca', 1998, 1000)
carro_2 = Carro(102, 'Sofia', 'Junho', 25000, 'Civic', 2021, 1500)
carro_3 = Carro(103, 'Lucas', 'Julho', 30000, 'HB20', 2019, 1200)
carro_4 = Carro(104, 'Isabela', 'Agosto', 35000, 'Corolla', 2020, 1800)
carro_5 = Carro(105, 'Marcela', 'Setembro', 28000, 'Golf', 2017, 1100)
carro_6 = Carro(106, 'Fernando', 'Outubro', 32000, 'Onix', 2020, 1300)
carro_7 = Carro(107, 'Camila', 'Novembro', 27000, 'Creta', 2019, 1400)
carro_8 = Carro(108, 'Gustavo', 'Dezembro', 30000, 'Siena', 2018, 1600)
carro_9 = Carro(109, 'Amanda', 'Janeiro', 31000, 'Argo', 2021, 1500)
carro_10 = Carro(110, 'Ricardo', 'Fevereiro', 29000, 'Cruze', 2019, 1700)
carro_11 = Carro(111, 'Luana', 'Março', 34000, 'Toro', 2022, 1800)
carro_12 = Carro(112, 'Pedro', 'Abril', 33000, 'Kicks', 2020, 1900)
carro_13 = Carro(113, 'Bianca', 'Maio', 35000, 'Ranger', 2021, 2000)
carro_14 = Carro(114, 'Marcos', 'Junho', 36000, 'Compass', 2018, 2100)


 
peca_1 = Peças(201, 'Pedro', 'Julho', 500, 'Motor', 'ABC123', 'Novo')
peca_2 = Peças(202, 'Lara', 'Agosto', 700, 'Pneu', 'XYZ789', 'Usado')
peca_5 = Peças(205, 'Mariana', 'Novembro', 700, 'Radiador', 'JKL012', 'Novo')
peca_6 = Peças(206, 'Roberto', 'Dezembro', 900, 'Freio', 'MNO345', 'Usado')
peca_7 = Peças(207, 'Tatiana', 'Janeiro', 600, 'Embreagem', 'PQR678', 'Recondicionado')
peca_8 = Peças(208, 'Eduardo', 'Fevereiro', 750, 'Correia Dentada', 'STU901', 'Semi-novo')
peca_9 = Peças(209, 'Fernanda', 'Março', 800, 'Catalisador', 'VWX234', 'Novo')
peca_10 = Peças(210, 'Guilherme', 'Abril', 850, 'Filtro de Óleo', 'YZA567', 'Usado')
peca_11 = Peças(211, 'Jéssica', 'Maio', 950, 'Sensor de Freio', 'BCD890', 'Recondicionado')
peca_12 = Peças(212, 'Vitor', 'Junho', 700, 'Amortecedor', 'EFG123', 'Semi-novo')
peca_13 = Peças(213, 'Patricia', 'Julho', 600, 'Bomba de Combustível', 'HIJ456', 'Novo')
peca_14 = Peças(214, 'Raul', 'Agosto', 700, 'Corpo de Borboleta', 'KLM789', 'Usado')


p1_taxa = peca_1.taxa()   
print(p1_taxa)
print(peca_1._valor )



#mesclat dados de banco de dados,puxar elementos associados a id,usando contadores e identificadores
#colocar tudo em tabelas ou excel para controle     


    
        


