import socket
import time

# Cria um socket para o servidor
servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor_endereco = ('localhost', 8888)  # Altere para o endereço desejado
servidor_socket.bind(servidor_endereco)
servidor_socket.listen(1)

print('Servidor pronto para receber conexões...')

while True:
    # Aceita uma conexão do cliente
    cliente_socket, cliente_endereco = servidor_socket.accept()
    print('Conexão estabelecida com:', cliente_endereco)

    # Recebe o tempo T0 enviado pelo cliente
    T0_cliente = cliente_socket.recv(1024).decode()
    
    print('T0_CLIENTE', T0_cliente)

    # Obtém o tempo atual correto T1
    T1_servidor = str(time.time())
    
    print('T1_CLIENTE', T1_servidor)

    # Calcula o ajuste T2 = T1 - T0
    T2_servidor = float(T1_servidor) - float(T0_cliente)
    
    print(T2_servidor)
    
    # Envia os tempos T0, T1 e T2 de volta para o cliente
    resposta = f"{T0_cliente},{T1_servidor},{T2_servidor}"
    cliente_socket.send(resposta.encode())

    # Fecha a conexão com o cliente
    cliente_socket.close()