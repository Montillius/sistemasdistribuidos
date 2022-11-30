import socket


def server_program():
    host = socket.gethostname() # um nome de host é um rótulo atribuído a um dispositivo conectado a uma rede de computadores é usado para identificar o dispositivo
    SERVER_PORT = 5000  # iniciando a porta acima da 1024

    server_socket = socket.socket()  # Instância do objeto do tipo socket

    #  Bind: realiza a associação entre a estrutura socket e o endereço/porta do servidor. Tomando como exemplo o
    #  diagrama da primeira figura deste tutorial, o comando “bind” vincula o endereço 10.1.1.1 do servidor e a porta 23
    #  ao socket que foi criado pelo sistema operacional do servidor.
    server_socket.bind((host, SERVER_PORT))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
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
