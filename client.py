import time
import random
import socket

# Define o tempo de atraso aleatório entre 0 e 60 segundos
atraso = random.randint(0, 60)

# Obtém o tempo T0 (tempo atual atrasado)
T0 = time.time() - atraso

print(T0)

# Converte o tempo para uma string legível
T0_formatado = time.ctime(T0)

# Cria uma conexão com o servidor
cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor_endereco = ('localhost', 8888)  # Altere para o endereço do servidor
cliente_socket.connect(servidor_endereco)

# Envia o tempo T0 para o servidor
T0_str = str(T0)
cliente_socket.send(T0_str.encode())

# Recebe os tempos T0, T1 e T2 do servidor
resposta = cliente_socket.recv(1024).decode()

T0_servidor, T1_servidor, T2_servidor = resposta.split(',')

# Fecha a conexão com o servidor
cliente_socket.close()

# Calcula a defasagem entre o tempo T0 e T1
defasagem = float(T2_servidor)

print(defasagem)

# Calcula o tempo atual ajustado
hora_ajustada = T0 + defasagem

print(hora_ajustada)

# Imprime a defasagem e o horário atual ajustado
print('Defasagem:', defasagem, 'segundos')
print('Horário atual ajustado:', time.ctime(hora_ajustada))