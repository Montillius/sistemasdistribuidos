import random  
# gerador de numeros aleatorios

from socket import *  
# sockets


# funcao que faz o calculo do numero de pontos
def pi(trials):
    hits = 0
    for i in xrange(trials):
        x = random.random()
        y = random.random()
        if (((x * x) + (y * y)) < 1):
            hits = hits + 1
    return hits


HOST = '192.168.1.110'
PORT = 7777

s = socket(AF_INET, SOCK_STREAM)  
# cria um socket

s.bind((HOST, PORT))  
# conecta o socket na porta

s.listen(1)  
# fica esperando conexoes

print('Escutando conexoes')
while 1:
    conn, addr = s.accept() 
    # recebe uma conexao
    
    data = conn.recv(1024)  
    # recebe o dado enviado pelo cliente
    
    if data == "PING":  
        # se o comando recebido foi um ping
        print("ping recebido")
        
    else:  
        # senao a informacao recebida eh o numero de tentativas
        
        print("Calculando para o cliente " + str(addr[0]))
        hits = pi(int(data))  
        # calcula o numero de pontos usando o numero de tentativas recebidas do cliente
        print(hits)
        conn.send(str(hits))  
        # retorna ao cliente o numero de pontos
        
        conn.close()  
        # fecha a conexao
