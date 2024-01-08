import abc


class Funcionario(abc.ABC):
    
    @abc.abstractclassmethod
    def nome(self):
        print('nome')

    @abc.abstractclassmethod
    def senha(self):
        print('senha')


#f = Funcionario()
#TypeError: Can't instantiate abstract class Funcionario with abstract method nome
#a classe mas não pode ser instanciada

class Atendente(Funcionario):
    def nome(self):
        return 'nome'

    def senha(self):
        print('senha')

a = Atendente() #da erro porque obriga a ter aquele emtodo
#print(a.nome) #saida:<bound method Atendente.nome of <__main__.Atendente object at 0x000001E1E5994710>>
print(a.nome()) #quando não é colocado () sai apenas o endereço da memoria
