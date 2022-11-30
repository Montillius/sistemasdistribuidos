import socket
from datetime import datetime


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
    # Ao estabelecer uma conexão com o clinte irá printar está conexão pro servidor

    while True:
        # condição que deve ser verdadeira, para continuar  a executar o servidor

        data = conn.recv(1024).decode()
        # Aguarda um dado enviado pela rede de até 1024 Bytes, a função ‘recv’ possui somente 1 argumento
        # que é o tamanho do Buffer.

        # Este método é usado para converter de um esquema de codificação, no qual a string de argumento é
        # codificada para o esquema de codificação desejado.

        data_sistema_americano = datetime.now()
        data_sistema_format = data_sistema_americano.strftime('%d/%m/%Y %H:%M:%S')
        # Configuração da hora do envio e recebimento das mensagens

        if not data:
            # O data irá receber a mensagem do cliente, se os dados não forem recebidos irá executar o break
            break
        print("O usuário conectado enviou: " + str(data))
        print('Hora atual do servidor ' + data_sistema_format)
        # Irá printar  a mensagem enviada pelo cliente e a hora atual do sistema

        data = input(' -> ') + (' Hora da mensagem: ' + data_sistema_format)
        # data que recebe a mensagem do servidor para enviar pro cliente, juntamente do horário
        conn.send(data.encode())
        # envia a mensagem do servidor para o cliente

    conn.close()
    # finaliza a conexão


if __name__ == '__main__':
    server_program()
