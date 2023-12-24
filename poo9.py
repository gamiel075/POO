class Contabancaria:


    number_of_users = 0
    lista_contas = []

    def __init__(self,ID,user_name,password,balance,value_debit,margin_of_balance):

        self.ID = ID
        self.__user_name = user_name
        self.__password = password
        self._balance = balance
        self.value_debit = value_debit
        self.__margin_of_balance = margin_of_balance
        self.__status = False
        self.__margin_of_balance = margin_of_balance
        self.history = []
        Contabancaria.number_of_users += 1
        Contabancaria.lista_contas.append(self)  # Adicionando o objeto à lista global



    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self,new_password):
        if isinstance(new_password, tuple) and len(new_password) == 2 and new_password[0] == self.__password:
            self.__password = new_password

        else:
            print('alteration not confirmed')


    def depositar(self,value):

        if(self.__status == True):
            if self._balance is not None:
                self._balance += value
                modificate = self._balance - value
                self.history.append((self._balance,value,modificate))
                print('deposit made')

        else:
            ('sorry, account no activate')

    def retirar(self,value):

        if(self.__status == True):
            if self._balance is not None:
                self._balance -= value
                modificate = self._balance - value
                self.history.append((self._balance,value,modificate))
                print('retirate made')
        else:
            ('sorry, account no activate')

    def _consult(self):

        password2 = int(input('digit your password for accessed'))
        if(password2 == self.__password):
                print(self._balance)


    

    


u1 = Contabancaria(555,'gabriel',111,150000,20000,50000)
u2 = Contabancaria(222,'miguel',222,250000,10000,30000)
u3 = Contabancaria(333,'rafael',2222,350000,20000,40000)
u4 = Contabancaria(111,'daniel',444,400000,30000,80000)

print(Contabancaria.number_of_users)
f





 
    








