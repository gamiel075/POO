
#itsnoright


from colorama import Fore,Back , Style, init
import matplotlib.pyplot as plt


class logisticontrol ():

    def __init__(self,password,stock_capacity,total_capacity,stored_quantity,productsinlost):

        self.password = password
        self.total_capacity = total_capacity #capacity total with sub utility
        self._stock_capacity = stock_capacity #capacity of stock
        self.stored_quantity = stored_quantity # quantility stored
        self.productsinlost = productsinlost #lost
        c1 = self.stored_quantity + self.productsinlost 
        self.empty_lease = self.total_capacity - c1 #quantility no stored
        self.subutility = self.total_capacity - self.stock_capacity #sub utility
        self.monthly_income = self.stored_quantity * 10


    

    def consult (self):

        
        
        print(f'capacity toatl:{self.total_capacity}')

        p1 =(self.total_capacity / 100) * 80
        p2  =(self.total_capacity / 100) * 60
        p3 = (self.total_capacity / 100) * 40
        p3 = (self.total_capacity / 100) * 40

        if(self._stock_capacity == p1 ):
            v1=  Fore.GREEN + str(self._stock_capacity)
            print(f'stock capacity(capacidade de locação):{v1}')
        
        elif(self._stock_capacity <  p1 and self._stock_capacity >= p2):
            v1 =  Fore.BLUE + str(self._stock_capacity)
            print(f'stock capacity(capacidade de locação):{v1}')

        elif(self._stock_capacity <  p2 and self._stock_capacity >= p3):
            v1=  Fore.YELLOW + str(self._stock_capacity)
            print(f'stock capacity(capacidade de locação):{v1}')
        
        elif( self._stock_capacity < p3):
            v1=  Fore.RED + str(self._stock_capacity)
            print(f'stock capacity(capacidade de locação):{v1}')


        
        a1 =(self.stock_capacity / 100) * 80
        a2  =(self.stock_capacity / 100) * 60
        a3 = (self.stock_capacity / 100) * 40
        a3 = (self.stock_capacity / 100) * 40

        if(self.stored_quantity == a1  ):
            v2=  Fore.GREEN + str(self.stored_quantity)
            print(f'stored quantity(quantidade armazenada):{v2}')


        elif(self.stored_quantity < a1 and self.stored_quantity >= a2 ):
            v2=  Fore.RED + str(self.stored_quantity)
            print(f'stored quantity(quantidade armazenada):{v2}')

        
        elif(self.stored_quantity <a2 and self.stored_quantity >= a3 ):
            v2=  Fore.YELLOW + str(self.stored_quantity)
            print(f'stored quantity(quantidade armazenada):{v2}')

        
        elif(self.stored_quantity < a3 ):
            v2=  Fore.GREEN + str(self.stored_quantity)
        
        print(f'products in lost:{self.productsinlost}')
        print(f'empty lease(resto não armazenado):{self.empty_lease}')
        print(f'total capacity of sub utility(quantidade da subutilidade): {self.subutility}')

    @property
    def total_capacity(self):
        return self._total_capacity
    
    @total_capacity.setter
    def total_capacity (self,new_total_capacity = []):
        if(new_total_capacity[0] == self.password):
            self._total_capacity = new_total_capacity[1]
        
        else:
            print('desculpe mas sua autenticação não foi validada')
            print('alteração não confirmada')

    @property
    def stock_capacity(self):
        return self._stock_capacity
    
    @stock_capacity.setter
    def stock_capacity (self,new_stock_capacity = []):
        if(new_stock_capacity[0] == self.password):
            self._stock_capacity = new_stock_capacity[1]

        else:
            print('desculpe mas sua autenticação não foi validada')
            print('alteração não confirmada')
            


    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, new_password):   
        if(new_password == self.password):
            self._password = new_password
            # Talvez você queira fazer algo com o terceiro elemento da tupla, se necessário, new_password[2]
        else:
            print('Desculpe, o formato da tupla de senha está incorreto.')
            print('Alteração não confirmada.') 


   
stored1 = logisticontrol((555), (120000), (90000), (75000), (7000))












    

        


    



    #password
    #month

    

    


    

    











        










    





            