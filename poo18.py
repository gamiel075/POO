class A:
    def m1(self):
        print('metodo a')

class B(A):
    def m2(self):
        print('metodo b')

class C(A):
    def m2(self):
        print('metodo c')

class D(B,C):
    pass 

d1=  D()
d1.m1()
d1.m2()  #LOSANGO
d1.m2()
#SAIDA:METODO B
#MRO 'Ordem de resolução de metodos
 

print(D.mro()) #saida: [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>] 







