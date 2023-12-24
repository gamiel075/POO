#testar get de uma forma siples


#atraves disto, pode -se estabelecer protocolos de mudança.


class pessoa():

    def __init__(self,nome,idade):
        
        self.nome = nome
        self._idade = idade
        self._status = False

    @property
    def marca(self):
        return self._nome
    
    @marca.setter
    def nome(self,novo__nome):
        self._nome = novo__nome


    def saudar(self):

        print(f'ola meu nome é {self.nome} e tenho {self._idade} anos')
        print(self._status)
    

    def set_nome(self,novo_nome):

       self._nome = novo_nome
       return self._nome

    def get_nome(self):
        return self._nome


    def set_idade(self,nova_idade):

        self._idade = nova_idade
        return self._idade

    def get_idade(self):
        return self._idade

    def set_status(self,novo_status):

        self._status = novo_status
        return self._status

        

    def get_status(self):

        return self._status
       
    def nova_saudaçao(self):

        print(f'ola meu nome é {self.__nome} e tenho {self._idade}')

    


myam = pessoa('gabriel',20)
myam.nome = 'LG'

print(myam.nome )

myam.saudar()
print('-----' * 10)






