class Rote:
    lista_roteiros = []  # Lista para armazenar os roteiros

    def __init__(self, id, ponto_partida, destino, distancia_km, dias_duracao, valor_carga, status):
        self.id = id
        self.ponto_partida = ponto_partida
        self.destino = destino
        self.distancia_km = distancia_km
        self.dias_duracao = dias_duracao
        self.valor_carga = valor_carga
        self.status = status

        # Adiciona automaticamente o objeto à lista de roteiros ao ser criado
        self.lista_roteiros.append(self)

    @classmethod
    def get_lista_roteiros(cls):
        return cls.lista_roteiros

# Exemplo de uso da classe Rote
# Aqui estou criando alguns objetos da classe Rote
r1 = Rote("r1", "São Paulo", "Rio de Janeiro", 200, 3, 5000, True)
r2 = Rote("r2", "Rio de Janeiro", "Belo Horizonte", 300, 4, 8000, False)
r3 = Rote("r3", "Belo Horizonte", "Brasília", 250, 2, 6000, True)

# Acesso à lista de roteiros diretamente através da classe
roteiros = Rote.get_lista_roteiros()

# Exibindo informações dos roteiros
for roteiro in roteiros:
    print(f"ID: {roteiro.id}, Partida: {roteiro.ponto_partida}, Destino: {roteiro.destino}, Distância: {roteiro.distancia_km} km, Dias de duração: {roteiro.dias_duracao}, Valor da carga: R${roteiro.valor_carga}, Status: {roteiro.status}")
