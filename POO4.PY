#ATIVADOR E VALIDDOR

class criar():

    def __init__(self,nome,senha,status = False ):

        self._nome = nome #o sinal de '_' impede que a mesma sofra quaisquer alteração externa
        self._senha = senha
        self._status = status


    def __informar(self): #existe mas não da pra usar

       return print(self._nome)  ,print(self._senha) ,print(self._status)
    
    def mostrar(self):

        print(self._nome)  
        print(self._senha) 
        print(self._status)




meunome = criar('gabriel',20)
  

#nada ver 


###########################################################



