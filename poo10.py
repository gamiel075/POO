
class ContaBancaria:

    number_of_users = 0

    def __init__(self, saldo):
        self.saldo = saldo
        ContaBancaria.number_of_users += 1

    @classmethod #isso aqui é para herança
    def getnumber_of_users(cls):
        print(ContaBancaria.number_of_users)
    
p1 = ContaBancaria(200)
p2 = ContaBancaria(200)

ContaBancaria.getnumber_of_users()


import random

class Rote:
    def __init__(self, id, ponto_partida, destino, distancia_km, dias_duracao, valor_carga, status):
        self.id = id
        self.ponto_partida = ponto_partida
        self.destino = destino
        self.distancia_km = distancia_km
        self.dias_duracao = dias_duracao
        self.valor_carga = valor_carga
        self.status = status

# Lista de cidades para uso nos pontos de partida e destinos
cidades = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Brasília", "Salvador", "Fortaleza", "Curitiba", "Manaus", "Belém", "Porto Alegre"]

# Lista para armazenar os roteiros
lista_roteiros = []

# Criar objetos de r1 a r15
for i in range(1, 16):
    ponto_partida = random.choice(cidades)
    destino = random.choice(cidades)
    distancia = random.randint(100, 500)
    duracao = random.randint(1, 5)
    carga = random.randint(3000, 15000)
    status = bool(random.getrandbits(1))

    roteiro = Rote(f"r{i}", ponto_partida, destino, distancia, duracao, carga, status)
    lista_roteiros.append(roteiro)

# Exibir informações dos roteiros criados
for roteiro in lista_roteiros:
    print(f"ID: {roteiro.id}, Partida: {roteiro.ponto_partida}, Destino: {roteiro.destino}, Distância: {roteiro.distancia_km} km, Dias de duração: {roteiro.dias_duracao}, Valor da carga: R${roteiro.valor_carga}, Status: {roteiro.status}")

r1 = Rote("r1", "São Paulo", "Rio de Janeiro", 200, 3, 5000, True)
r2 = Rote("r2", "Rio de Janeiro", "Belo Horizonte", 300, 4, 8000, False)
r3 = Rote("r3", "Belo Horizonte", "Brasília", 250, 2, 6000, True)
r4 = Rote("r4", "Brasília", "Salvador", 320, 3, 7500, False)
r5 = Rote("r5", "Salvador", "Fortaleza", 280, 4, 9000, True)
r6 = Rote("r6", "Fortaleza", "Curitiba", 400, 2, 7000, False)
r7 = Rote("r7", "Curitiba", "Manaus", 340, 3, 8200, True)
r8 = Rote("r8", "Manaus", "Belém", 290, 4, 5500, False)
r9 = Rote("r9", "Belém", "Porto Alegre", 380, 2, 6800, True)
r10 = Rote("r10", "Porto Alegre", "São Paulo", 270, 3, 7200, False)
r11 = Rote("r11", "Rio de Janeiro", "Brasília", 310, 4, 6100, True)
r12 = Rote("r12", "Belo Horizonte", "Salvador", 240, 2, 5300, False)
r13 = Rote("r13", "Brasília", "Fortaleza", 330, 3, 8400, True)
r14 = Rote("r14", "Salvador", "Curitiba", 370, 4, 9200, False)
r15 = Rote("r15", "Fortaleza", "Manaus", 260, 2, 6800, True)