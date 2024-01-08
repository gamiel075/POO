

class Funcionarios:
    def __init__(self,nome,cpf,salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario

    def bonus(self):
        return self._salario * 1.2

        #conceito de é um,todos os elementos abaixos são Um Funcionários


class Gerente(Funcionarios):
    def __init__(self,nome,cpf,salario,senha,qtd_colab):
        super().__init__(nome,cpf,salario) 
        self.__senha = senha
        self.qtd_colab = qtd_colab
        #modificadores

    def get_nome(self):
        return self._nome

    def bonus(self):
        return self._salario * 1.2 + self.qtd_colab * 0.10


    def validar(self,senha1):
        if (self.__senha == senha1):
            print('Acesso permitido')
            return True
        else:
            print('acesso Negado')
            return False
        
    def printar(self):
        d1 = {'nome':self._nome,'cpf':self._cpf,'saalrio':self._salario}
        print(d1) #saida = {'nome': 'cladio', 'cpf': 6565545544, 'saalrio': 20000}

         

class Secretaria(Funcionarios):
    def __init__(self,nome,cpf,salario,senha,qtd_gerentes):
        super().__init__(nome,cpf,salario)
        self.__senha = senha
        self.qtd_gerentes = qtd_gerentes

    def bonus(self):
        return self._salario * 1.2 + self.qtd_gerentes * 0.5
    

class Engenheiro:
    def __init__(self,nome):
        self._nome = nome

    


class ClubeGerentes:

    def __init__(self, nome, FuncionarioS):
        self.nome = nome
        self._funcionarios = FuncionarioS

    def __getitem__(self,item):
        return self._funcionarios[item]
    
    def __len__(self):
        return len(self._funcionarios)  # Retornar o comprimento da lista de funcionários


    def listagem(self):
        return self._funcionarios  # Retorna a lista de funcionários em vez de apenas imprimi-la
    
    def tamanho(self):
        print(len(self._funcionarios))



class GestãoDeBonus():

    def __init__(self,total_bonifiacacoes = 0 ):
        self._total_bonifiacoes = total_bonifiacacoes

    def registra(self,Funcionario):
        if(hasattr(Funcionario,'bonus()')):
            self._total_bonifiacoes += Funcionario.bonus()
        else:
            print('o objeto não tem essa implementação')

    #esse conceito pode servir para B.I porque pode se estudar e avaliar as alterações re


    @property
    def total_bonifiacacoes(self):
        print(self._total_bonifiacoes)
    

# def __init__(self,nome,cpf,salario,senha,qtd_colab):
g1 = Gerente('claudio',124643,5000,333,7)
g2 = Gerente('maria',55555,75001444,111,10)
g3 = Gerente('joao',33333,756554,222,15)

lista_gerentes = [g1,g2,g3]
clube = ClubeGerentes('clube top',lista_gerentes)
clube.listagem()


for g in clube:
    print(g.get_nome())  # Use o método get_nome() para acessar o nome do gerente 

print(len(clube))
print(clube[1].get_nome())
#saida:maria

from abc import ABC
from collections.abc import MutableSequence

class Secretaryclub(MutableSequence):
    def __delitem__(self,item):
        print('delete')

    def __getitem__(self,item):
        print('coleta')

    def __len__(self) -> int:
        return super().__len__()
    def __setitem__(self):
        return print('len')
    
    def insert(self):
        print('')

#cs = Secretaryclub() #saida antes: TypeError: Can't instantiate abstract class Secretaryclub with abstract methods __delitem__, __getitem__, __len__, __setitem__, insert
#cs = Secretaryclub() saida depois  TypeError: Can't instantiate abstract class Secretaryclub with abstract methods __len__, __setitem__, insert#
cs = Secretaryclub() #saida normal pois nos estavamos obrigando ela a ter uma interface
























    

    

    

    









    

    






#carnes / #frutas #bebidas e etc








