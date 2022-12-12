import threading
import socket


# processos que rodam paralelamente
# função rodando ao lado de outra função
def main():
    # função principal
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # definindo ipv4 e tcp
    try:
        client.connect(('localhost', 7777))
        # tentar conectar ao servidor
    except:
        return print('\nNão foi possívvel se conectar ao servidor!\n')
        # quebra a função main e printa  o resultado
    username = input('Usuário> ')
    print('\nConectado')
    # definir os nomes de cada usuário e avisar que está conectado  
    thread1 = threading.Thread(target=receiveMessages, args=[client])
    # target define o que vai executar
    thread2 = threading.Thread(target=sendMessages, args=[client, username])

    thread1.start()
    thread2.start()
    # executar as funções ao mesmo tempo


def receiveMessages(client):
    # enquanto estiver conectado, sempre vai receber algo do servidor
    while True:
        try:
            msg = client.recv(2048).decode('utf-8')
            # decode transformar de bytes para string
            print(msg + '\n')
        except:
            print('\nNão foi possível permanecer conectado no servidor!\n')
            print('Pressione <Enter> Para continuar...')
            # input pega a tecla enter e retorna fechando a função
            client.close()
            break


def sendMessages(client, username):
    while True:
        # vai entrar no laço de repetição e captar o que cada usuário digitar
        try:
            msg = input('\n')
            client.send(f'<{username}> {msg}'.encode('utf-8'))
            # encode transformar string em bytes
        except:
            return


main()
