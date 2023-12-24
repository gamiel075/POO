#primeira saida: ola meu nome é gabriel e tenho 20 anos . false
new_name = myam.set_nome('miguel')
print(myam.get_nome())
new_age = myam.set_idade(11)
print(myam.get_idade())
new_status = myam.set_status(True)
print(myam.get_status())
print('-----' * 10)
myam.nova_saudaçao()


class RegistroVariavel:
    def __init__(self):
        self.valor_atual = None
        self.historico = []

    def alterar_valor(self, novo_valor):
        if self.valor_atual is not None:
            mudanca = novo_valor - self.valor_atual
            self.historico.append((self.valor_atual, novo_valor, mudanca))
        self.valor_atual = novo_valor

    def obter_historico(self):
        return self.historico

# Exemplo de uso:
registro = RegistroVariavel()

# Alterações de valor ao longo do tempo
registro.alterar_valor(50)
registro.alterar_valor(75)
registro.alterar_valor(100)
registro.alterar_valor(80)

# Obtendo o histórico de alterações
historico = registro.obter_historico()
for antigo, novo, mudanca in historico:
    print(f"Valor antigo: {antigo}, Novo valor: {novo}, Mudança: {mudanca}")


#saber quem e quando alterou

def extract(self):
        return self.history
  
    def extract2(self): 
        historico = object.extract()
        for antigo, novo, mudanca in historico:
            print(f"Valor antigo: {antigo}, Novo valor: {novo}, Mudança: {mudanca}")




555,gabriel,150000,20000,50000
 