import socket
from datetime import datetime


def client_program():
    host = socket.gethostname()
    # o host irá receber o conexão com o servidor para que o encontre

    PORTA = 5000
    # Usando a mesma analogia do serverP, a porta é por onde de fato os pacotes "entram" no servidor ou seja
    # é necessário que seja a mesma para que ocorra a comunicação

    client_socket = socket.socket()
    # Instância do objeto do tipo socket no formatto TCP/IP

    client_socket.connect((host, PORTA))
    # a fução connect estabele a conexão com o servidor
    # Quando a connect (conexão) foi estabelecida, o soquete pode ser utilizado para enviar uma solicitação de
    # texto para o servidor. O mesmo soquete é que irá ler a resposta.

    message = input(' -> ')
    # Entrada da mensagem

    while message.lower().strip() != 'finalizar serviço':
        # loop criado para deixa o programa em execução se o clientP enviar a mensagem 'finalizar serviço'
        # o loop encerrará. O metofo lower transforma todos os caracteres em minusculos e o strip procura dentro
        # da mensagem o texto que foi especificado

        if message == '':
            message = '\n'
            client_socket.send(message.encode())
        else:
            client_socket.send(message.encode())
        # envia a mensagem do cliente para o servidor

        data = client_socket.recv(1024).decode()
        #  Aguarda um dado respondido pelo servidor de até 1024 Bytes, a função ‘recv’ possui somente 1 argumento
        # que é o tamanho do Buffer.

        print('Resposta do servidor: ' + data)
        # Irá printar  a mensagem recebida do servidor

        message = input(' -> ')
        # exibe novamente a entrada de dados para que o cliente se comunique, enquanto a condição for verdadeira
        # irá ser executado

    client_socket.close()
    # finaliza a conexão com o servidor


if __name__ == '__main__':
    client_program()
