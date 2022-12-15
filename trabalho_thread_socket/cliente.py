import socket
import threading

HOST = '10.0.0.206'
# o host tem que utilizar o endereço do servidor para se conectar

PORTA = 8383
# Usando a mesma analogia do server, a porta é por onde de fato os pacotes "entram" no servidor ou seja
# é necessário que seja a mesma porta para que ocorra a comunicação e troca de dados

client_socket = socket.socket()
# Instância do objeto do tipo socket no formatto TCP/IP

client_socket.connect((HOST, PORTA))


# a fução connect estabele a conexão com o servidor
# Quando a connect (conexão) foi estabelecida, o soquete pode ser utilizado para enviar uma solicitação de
# texto para o servidor. O mesmo soquete é que irá ler a resposta.


# Função para verificar se um número é primo
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


# Função que executa a thread
def thread_function(start, end):
    # Lista para armazenar os números primos encontrados
    prime_numbers = []

    # Verifica cada número no intervalo especificado
    for i in range(start, end):
        if is_prime(i):
            prime_numbers.append(i)

    print(prime_numbers)
    client_socket.send(str(prime_numbers).encode())


# Cria as threads
thread1 = threading.Thread(target=thread_function, args=(1, 5000))

# Inicia as thread
thread1.start()
