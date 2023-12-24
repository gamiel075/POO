class Faltura:
    def __init__(self,comprimento,largura,nome):

        self._comprimento = comprimento
        self.largura = largura
        self.__nome = nome

    def _calculaArea(self):
        print(self._comprimento * self.largura)
        print(f'{self.__nome}name user what solicited the operation')


#agora vc não se confunde
    


    
c1 = Faltura(10,20,'gabriel')
#print(c1.__nome ) #assim o atributo esta privado,portanto da erro 
print(c1._comprimento) #saida = 10
#print(c1.__nome) #da erro mas ele fnciona dentro da classe

c1._calculaArea()


print(dir(Faltura)) #saida = ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
#'__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_calculaArea']#
    




        