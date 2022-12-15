import socket
import threading

HOST = '10.0.0.206'
# o host tem que utilizar o endereço do servidor para se conectar

PORTA = 8585
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
thread = threading.Thread(target=thread_function, args=(1, 10000))
thread2 = threading.Thread(target=thread_function, args=(10001, 20000))
thread3 = threading.Thread(target=thread_function, args=(20001, 30000))
thread4 = threading.Thread(target=thread_function, args=(30001, 40000))
thread5 = threading.Thread(target=thread_function, args=(40001, 50000))
thread6 = threading.Thread(target=thread_function, args=(50001, 60000))
thread7 = threading.Thread(target=thread_function, args=(60001, 70000))
thread8 = threading.Thread(target=thread_function, args=(70001, 100000))

# Inicia as thread
thread.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
thread6.start()
thread7.start()
thread8.start()
