import socket


def server_program():
    host = '10.0.0.203'
    # um nome de host é um rótulo atribuído a um dispositivo conectado a uma rede de computadores é usado
    # para identificar o dispositivo
    SERVER_PORT = 5000
    # iniciando a porta acima da 1024

    server_socket = socket.socket()
    # Instância do objeto do tipo socket no formatto TCP/IP

    server_socket.bind((host, SERVER_PORT))
    #  Bind: realiza a associação entre a estrutura socket e o endereço/porta do servidor.
    #  O comando “bind” vincula o endereço como exemplo 10.1.1.1 do servidor e a porta 5000
    #  ao socket que foi criado pelo sistema operacional do servidor.


    server_socket.listen(1)
    # O nosso servidor TCP/IP vai receber 1 conexão por vez e responder ao cliente uma confirmação do recebimento
    # da mensagem. A função listen() coloca o socket no modo servidor, e define a quantidade de solicitações
    # de novas conexões que podem ser enfileiradas.

    conn, address = server_socket.accept()
    # A função accept() retorna um novo socket para ser usado com aquela conexão e, o endereço do cliente.
    # O novo socket utiliza uma nova porta atribuída automaticamente pelo kernel.

    print("Conexão de: " + str(address))
    while True:
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        print("from connected user: " + str(data))
        data = input(' -> ')
        conn.send(data.encode())  # send data to the client

    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()
