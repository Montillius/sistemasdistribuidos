# Servidor TCP
# importa a biblioteca socket
import socket

# Porta que o Servidor vai escutar
ports = [5003, 5004]
host = ['', '']
tcpSockets = []
conns = []
clients = []

# criação do socket
# af_inet = suporte para dominio de intener tipo notacao de site ou ipv4 / sock_stream = cria um objeto de socket do tipo TCP
for idx in range(2):
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp.bind((host[idx], ports[idx]))
    tcp.listen(1)
    tcpSockets.append(tcp)

print("Servidor rodando...")

for tcp in tcpSockets:
    index = tcpSockets.index(tcp)
    con, client = tcp.accept()
    conns.append(con)
    conns[index].send(str(index + 1).encode())
    clients.append(client)
    print('Conectado por ', clients[index])

resul_parcial1 = float(conns[0].recv(4096))
resul_parcial2 = float(conns[1].recv(4096))

print("\nValor parcial da equação recebido do client 01: ", resul_parcial1)
print("\nValor parcial da equação recebido do client 02: ", resul_parcial2)

areaTotal = resul_parcial2 + resul_parcial1

print("\nResultado final (Area Total): ", areaTotal)
