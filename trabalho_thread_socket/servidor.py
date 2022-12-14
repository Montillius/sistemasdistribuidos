# Disciplina: Sistemas Distribuidos (2022.2)
# Professor: LEONARDO BARRETO CAMPOS
# Dupla: Luan Rangel e Otiliano Junior

# Tema: Números primos com Threads e sockets
#  -----------------------------------------------------------------------------------------------------------------

import socket

ports = [5003, 5004]
# As portas permitem que os servidores diferenciem facilmente entre diferentes tipos de tráfego:
# os e-mails vão para uma porta diferente daquela das páginas web, por exemplo,
# É importe que seja instanciado em um valor acima de 1024, para que não haja conflito entre as demais portas já usadas
# pela maquina, neste caso usaremos ma porta pra cada cliente

host = ['', '']
# um nome de host é um rótulo atribuído a um dispositivo conectado a uma rede de computadores é usado
# para identificar o dispositivo, aqui não estamos passando valor para o host, pois quem precisa sabe 
# em qual servidor conectar é o cliente

lista_server_socket = []
# Lista destinada aos sockets de conexão do servidor

lista_conns = []
# lista de conexões

lista_clients = []
# lista de clientes


for i in range(2):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Instância do objeto do tipo socket no formatto TCP/IP
    #  Como padrão a biblioteca socket do python faz essa implementação
    # af_inet = suporte para dominio de intener tipo notacao de site ou ipv4
    # sock_stream = cria um objeto de socket do tipo TCP

    server_socket.bind((host[i], ports[i]))
    #  O comando “bind” vincula o endereço como exemplo 10.1.1.1 do servidor e a porta 5000
    #  ao socket que foi criado pelo sistema operacional do servidor.

    server_socket.listen(1)
    # O nosso servidor TCP/IP vai receber 1 conexão por vez.
    # A função listen() 'ouvindo' coloca o socket no modo servidor, e define a quantidade de solicitações
    # de novas conexões que podem ser enfileiradas.

    lista_server_socket.append(server_socket)
    # adciona o socket do sercer na lista

print("Servidor rodando...")

for server_socket in lista_server_socket:
    index = lista_server_socket.index(server_socket)
    con, client = server_socket.accept()
    # A função accept() retorna um novo socket para ser usado com aquela conexão e, o endereço do cliente.
    # neste caso sera executado para cada conexão que possuir na lista de sockets
    lista_conns.append(con)
    lista_clients.append(client)

    print('Conectado por ', lista_clients[index])
    # Ao estabelecer uma conexão com o clinte irá printar está conexão pro servidor

result_client1 = str(lista_conns[0].recv(16384).decode())
# Aguarda a resposta do cliente 1, a quantidade de bytes é escolhida pelo usuário

result_client2 = str(lista_conns[1].recv(16384).decode())
# Aguarda a resposta do cliente 1, a quantidade de bytes é escolhida pelo usuário


lista_primos = result_client2 + result_client1
# O resultado final obtido pelos dois clientes


print('Lista de primos de 1 a 5000 ', lista_primos)
