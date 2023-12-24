
import matplotlib.pyplot as plt
from colorama import Fore, Style

class Logisticontrol():
    def __init__(self, password, total_capacity,stock_capacity, stored_quantity, productsinlost):
        self.__password = password
        self._total_capacity = total_capacity
        self._stock_capacity = stock_capacity
        self.stored_quantity = stored_quantity
        self.productsinlost = productsinlost
        self.empty_lease = self.total_capacity - (self.stored_quantity + self.productsinlost)
        self.subutility = self.total_capacity - self.stock_capacity
        self.monthly_income = self.stored_quantity * 10


    def consult(self):

        print(f'capacity toatl:{self.total_capacity}')

        print('-----'* 10)

        p1 = (self.total_capacity / 100) * 80
        p2  =(self.total_capacity / 100) * 60
        p3 = (self.total_capacity / 100) * 40
        p4 = (self.total_capacity / 100) * 20

        if(self._stock_capacity == p1  or self._stock_capacity > p1):
            v1=  Fore.GREEN + str(self._stock_capacity)
            print(f'stock capacity(capacidade de locação):{v1}')
            print(Style.RESET_ALL)

            
        
        elif(self._stock_capacity <  p1 or self._stock_capacity >= p2):
            v1 =  Fore.BLUE + str(self._stock_capacity)
            print(f'stock capacity(capacidade de locação):{v1}')
            print(Style.RESET_ALL)


        elif(self._stock_capacity <  p2 or  self._stock_capacity >= p3):
            v1=  Fore.YELLOW + str(self._stock_capacity)
            print(f'stock capacity(capacidade de locação):{v1}')
            print(Style.RESET_ALL)

        
        elif( self._stock_capacity < p4):
            v1=  Fore.RED + str(self._stock_capacity)
            print(f'stock capacity(capacidade de locação):{v1}')
            print(Style.RESET_ALL)



        
        a1 =(self.stock_capacity / 100) * 80
        a2  =(self.stock_capacity / 100) * 60
        a3 = (self.stock_capacity / 100) * 40
        a4 = (self.stock_capacity / 100) * 20

        if(self.stored_quantity == a1 or self.stored_quantity > a1 ):
            v2=  Fore.GREEN + str(self.stored_quantity)
            print(f'stored quantity(quantidade armazenada):{v2}')
            print(Style.RESET_ALL)



        elif(self.stored_quantity < a1 or self.stored_quantity >= a2 ):
            v2=  Fore.BLUE + str(self.stored_quantity)
            print(f'stored quantity(quantidade armazenada):{v2}')
            print(Style.RESET_ALL)


        
        elif(self.stored_quantity <a2 or self.stored_quantity >= a3 ):
            v2=  Fore.YELLOW + str(self.stored_quantity)
            print(f'stored quantity(quantidade armazenada):{v2}')
            print(Style.RESET_ALL)



        elif(self.stored_quantity < a3 ):
            v2=  Fore.RED + str(self.stored_quantity)
            print(f'stored quantity(quantidade armazenada):{v2}')
            print(Style.RESET_ALL)

       
        print('-----' *10)    
        
        print(f'products in lost:{self.productsinlost}')
        print(f'empty lease(resto não armazenado):{self.empty_lease}')
        print(f'total capacity of sub utility(quantidade da subutilidade): {self.subutility}')


    @property
    def total_capacity(self):
        return self._total_capacity

    @total_capacity.setter
    def total_capacity(self, new_total_capacity):
        if isinstance(new_total_capacity, tuple) and len(new_total_capacity) == 3 and new_total_capacity[0] == self.__password:
            self._total_capacity = new_total_capacity[1]
        else:
            print('Desculpe, a autenticação falhou ou o formato da tupla está incorreto.')
            print('Alteração não confirmada.')

    @property
    def stock_capacity(self):
        return self._stock_capacity

    @stock_capacity.setter
    def stock_capacity(self, new_stock_capacity):
        if isinstance(new_stock_capacity, tuple) and len(new_stock_capacity) == 3 and new_stock_capacity[0] == self.__password:
            self._stock_capacity = new_stock_capacity[1]
        else:
            print('Desculpe, a autenticação falhou ou o formato da tupla está incorreto.')
            print('Alteração não confirmada.')




    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, new_password):
        if isinstance(new_password, tuple) and len(new_password) == 3:
            self.__password = new_password[0]
        else:
            print('Desculpe, o formato da tupla de senha está incorreto.')
            print('Alteração não confirmada.')

    def getstored(self):
        return self.stored_quantity

    def setstored(self,new_stored):
        self.stored_quantity = new_stored
        
    stored = property(fget = getstored , fset = setstored)



    

stored1 = Logisticontrol((555), (120000), (90000), (75000), (7000))
# as alterações property estão validades, as alterações são feitas apenas com a validação


stored1.consult()


#fazer condicionais dos demais selfs.
#um historico de alteração






