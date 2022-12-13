from socket import *
import sys
import time
from threading import Thread

PORT = 7777


class cliente(Thread):
    # subclasse da classe Thread. essa classe conecta com o servidor e envia os dados para serem calculados
    def __init__(self, ip, trials):
        # construtor da classe

        Thread.__init__(self)
        # chama o construtor da classe pai

        self.ip = ip
        # o ip que deve conectar

        self.hits = -1
        # armazena o resultado

        self.trials = str(trials)
        # numero de tentativas

    def run(self):
        # essa eh a parte que serah executada

        print("thread do ip " + str(self.ip) + " iniciou")
        # abre a conexao com o servidor

        s = socket(AF_INET, SOCK_STREAM)
        s.connect((self.ip, PORT))
        # envia para o servidor o numero de tentativas

        s.send(self.trials)
        # fica esperando o resultado do calculo do servidor

        self.hits = s.recv(1024)
        s.close()
        print("trhread do ip " + str(self.ip) + " finalizou com o resultado=" + str(self.hits))


def ativos(servidores):
    # funcao que verifica se os servidores estao ativos

    ativos = []
    # lista com os servidores ativos

    for ip in servidores:
        try:
            print("testando " + str(ip))
            s = socket(AF_INET, SOCK_STREAM)
            s.connect((ip, PORT))
            s.send("PING")
            # manda um comando ping para ver se o servidor ainda esta ativo
            s.close()
            ativos.append(ip)
        except:
            # print "Unexpected error:", sys.exc_info()[0]
            pass
        return ativos


trials = sys.argv[0]
# recebe do parametro do usuario o numero maximo de tentativas

print("Verificando servidores ativos")
# verifica o numero de servidores ativos

servidores = ativos(['192.168.1.110', '200.135.240.1', '192.168.200.11', '192.168.200.5'])

if len(servidores) == 0:
    print("Nao existem servidores ativos")
    sys.exit()

print("Servidores ativos:" + str(servidores))
# calcula o numero de tentativas que cada servidor deve executar

trials_por_servidor = int(trials) / len(servidores)

resultado = []
# lista com as threads em execucao

t0 = time.time()
# usado para o calculo do tempo de execucao

for ip in servidores:
    atual = cliente(ip, trials_por_servidor)
    # cria uma nova thread

    resultado.append(atual)
    # adiciona a thread na lista de threads

    atual.start()
    # inicia a thread

total_hits = 0
# total dos resultados

for r in resultado:
    r.join()
    # espera ate a thread terminar
    total_hits += int(r.hits)

pi = 4.0 * int(total_hits) / int(trials)
# faz o calculo do pi usando os resultados enviados por cada servidor
print("Pi :" + str(pi))
tf = time.time()
print('O tempo gasto na execucao eh: ', tf - t0, '[s]')
