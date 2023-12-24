
class People():

    def __init__(self,id_people,name,age,):

        self.id_people = id_people
        self.nome = name
        self.__age = age

    @property
    def nome(self):
        return self._nome
    
    
    @nome.setter
    def nome(self,new_name):
        self._nome = new_name


    def setage(self,new_age):
        self.__age = new_age

    def getage (self):
        return self.__age

    def view (self):
         dictionary = {'name': self.nome ,'age':self.__age,'id':self.id_people }
         print(dictionary)


    age = property(fget = getage , fset= setage)



gabriel = People('555','gabriel',20)
gabriel.view() #saida = {'name': 'miguel', 'age': 20, 'id': '555'}
gabriel.age = 21 
print(gabriel.age)
gabriel.nome = 'miguel'
gabriel.view()   #saida = {'name': 'miguel', 'age': 20, 'id': '555'}





