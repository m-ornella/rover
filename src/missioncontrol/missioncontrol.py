import socket

client= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 8080))

client.send('Hello From Client'.encode())
print(client.recv(1024))