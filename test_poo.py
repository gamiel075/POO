

class InformacoesEncomenda:
    def __init__(self):
        self.lista_encomendas = []

    def adicionar_encomenda(self, encomenda):
        if isinstance(encomenda, Encomenda) or isinstance(encomenda, Carro) or isinstance(encomenda, Peças):
            self.lista_encomendas.append({
                'id_encomenda': encomenda.id,
                'nome_destinatario': encomenda._nome_destinatario,
                'quantidade_compras': encomenda.quantidade_compras if hasattr(encomenda, 'quantidade_compras') else None
            })

# Supondo que Encomenda, Carro e Peças sejam suas classes definidas

# Criando instâncias das classes Encomenda, Carro e Peças
encomenda = Encomenda(1, 'Destinatario 1', 'Janeiro', 100)
carro = Carro(2, 'Destinatario 2', 'Fevereiro', 200, 'Modelo', 2022, 500)
pecas = Peças(3, 'Destinatario 3', 'Março', 300, 'Nome Peça', 'Modelo', 'Bom')

# Criando uma instância de InformacoesEncomenda e adicionando as instâncias das outras classes
informacoes = InformacoesEncomenda()
informacoes.adicionar_encomenda(encomenda)
informacoes.adicionar_encomenda(carro)
informacoes.adicionar_encomenda(pecas)

# Acessando as informações reunidas
for encomenda_info in informacoes.lista_encomendas:
    print(encomenda_info)




