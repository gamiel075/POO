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


    




g1 = Gerente('claudio',124643,5000,333,7)
       #limitar mudanças e colocar validadores 
#g1._cpf =  6565545544
#g1._salario = 20000
g1.printar()
#############################################
s1 = Secretaria('gabriela',456555,2000,555,5)
print(s1._nome) #saida = gabriela
######################################
g2 = Gerente('caio',265565,3500,222,9)
s2 = Secretaria('maria',456555,2000,555,5)

g2_bonus = g2.bonus()
print(g2_bonus)
#saida = 4200 antes
#saida = 4200.9
#por issso a importancia dos dicionarios, eles dinamizam os dados.
s2_bonus = s2.bonus()
print(s2_bonus)
#saida:2400.0 # antes
#saida: 2402.5 






