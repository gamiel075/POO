


class Contabancaria:


    number_of_users = 0

    def __init__(self,ID,user_name,password,balance,value_debit,margin_of_balance):

        self.ID = ID
        self.__user_name = user_name
        self.__password = password      #aproveite privado e protegido para criar varias ideias
        self._balance = balance
        self.value_debit = value_debit
        self.__margin_of_balance = margin_of_balance
        self.__status = False
        self.__margin_of_balance = margin_of_balance
        self.history = []
        Contabancaria.number_of_users += 1
         # Adicionando o objeto à lista global


    def getnumber_of_users(self):
        print(Contabancaria.number_of_users)

    def getstatus(self):
        return self.__status
    
    def setstatus(self,new_status):
          
        password2 = float(input('digit your password for accessed'))
        if(password2 == self.__password):
            self.__status = new_status

    status = property(fget = getstatus,fset = setstatus)



    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self,new_password):
        if isinstance(new_password, tuple) and len(new_password) == 2 and new_password[0] == self.__password:
            self.__password = new_password

        else:
            print('alteration not confirmed')


    def depositar(self):
                
        question1=float(input('digit your password for accessed'))
        if(question1 == self.__password):
            value = float(input('digit value of deposit'))         
            self._balance += value
            print('deposit made')
            modificate = self._balance - value
            self.history.append((self._balance,value,modificate))
            print('deposit made')

        else:
            ('sorry, account no activate')

    def retirar(self,value):
                
        question1=float(input('digit your password for accessed'))
        if(question1 == self.__password):
            value = float(input('digit value of retirat'))      
            self._balance -= value
            modificate = self._balance - value
            self.history.append((self._balance,value,modificate))
            print('retirate made')
        else:
            ('sorry, account no act ivate')

    def _consult(self):

        password2 = float(input('digit your password for accessed'))
        if(password2 == self.__password):
            print(self._balance)
            for transaction in self.history:
                print(transaction) 
        else:
            print('password erro')

    def post(self,lista_contas):

        return lista_contas


    @staticmethod
    def validador(id):
        return len(str(id)) == 2
        #da pra criar um metodo que valide algo da conta ou da oepração do cliente
        #como também da pra criar algo especifico sobre a classe e armazenar em algum lugar

        #da pra criar um monitor e um converson também caso precise ou simulador
    
        

            
#valores = id / name / password......
u1 = Contabancaria(555,'gabriel',111,150000,25000,50000)
u2 = Contabancaria(222,'miguel',222,250000,10000,30000)
u3 = Contabancaria(333,'rafael',2222,350000,20000,40000)
u4 = Contabancaria(111,'daniel',444,400000,30000,80000)
u5 = Contabancaria(888,'samuel',666,600000,90000,70000)

Contabancaria.getnumber_of_users(u1)

u1.status = True
u1.depositar()
u1._consult()
validar = u1.validador(u1)
print(validar) #saida False




class ContaBancaria:
    taxa_conversao = 0.2  # Taxa de conversão de moeda

    def __init__(self, saldo):
        self.saldo = saldo

    @staticmethod
    def converter_para_dolar(valor_em_real):
        return valor_em_real * ContaBancaria.taxa_conversao
    
saldo_em_real = 1000
saldo_em_dolar = ContaBancaria.converter_para_dolar(saldo_em_real)
print(f"Saldo em dólar: ${saldo_em_dolar}")
#exemplo metodo estatico

















 
    








