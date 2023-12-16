#testar get de uma forma siples




class pessoa():

    def __init__(self,nome,idade):
        
        self._nome = nome
        self._idade = idade
        self._status = False


    def saudar(self):

        print(f'ola meu nome é {self._nome} e tenho {self._idade} anos')
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

        print(f'ola meu nome é {self._nome} e tenho {self._idade}')

    





myam = pessoa('gabriel',20)
myam.saudar()
print('-----' * 10)
#primeira saida: ola meu nome é gabriel e tenho 20 anos . false
new_name = myam.set_nome('miguel')
print(myam.get_nome())
new_age = myam.set_idade(11)
print(myam.get_idade())
new_status = myam.set_status(True)
print(myam.get_status())
print('-----' * 10)
myam.nova_saudaçao()





