class Documentos:
    def __init__(self, id, valor, tipo_titulo):
        self.id = id
        self.valor = valor
        self.tipo_titulo = tipo_titulo

class Mensalidade(Documentos):
    pass

class Compras(Documentos):
    pass

class Fatura:
    def __init__(self, mensalidade, compras):
        self.mensalidade = mensalidade
        self.compras = compras

    def calcular_total(self):
        total = 0
        if hasattr(self.mensalidade, 'valor'):
            total += self.mensalidade.valor
        if hasattr(self.compras, 'valor'):
            total += self.compras.valor
        return total

    def calcular_novo_id(self):
        total_ids = 0
        if hasattr(self.mensalidade, 'id'):
            total_ids += self.mensalidade.id
        if hasattr(self.compras, 'id'):
            total_ids += self.compras.id
        return total_ids

# Criando objetos
m1 = Mensalidade(1, 100, 'Mensal')
c1 = Compras(2, 150, 'Compra')

# Criando uma fatura com as mensalidades e compras
fatura = Fatura(m1, c1)

# Calculando valores
total_fatura = fatura.calcular_total()
novo_id_fatura = fatura.calcular_novo_id()

print(f"Total da fatura: {total_fatura}")
print(f"Novo ID da fatura: {novo_id_fatura}")



