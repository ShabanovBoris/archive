import socket,json
sock = socket.socket()
sock.connect(('localhost',9091))
print(sock.recv(1024).decode())
lenght=int(sock.send(input().encode()))
i=0
while i < lenght:
    print(sock.recv(1024).decode())
    sock.send(input().encode())
print(sock.recv(1024).decode())
choice=int(sock.send(input().encode()))
i=0
if choice == 1:
    print(sock.recv(1024).decode())
    sock.send(input().encode())
    data = sock.recv(4096)
    data_arr = json.loads(data.decode())
    print(sock.recv(1024).decode())
elif choice == 0:
    print(sock.recv(1024).decode())
    lenghtIndex = int(sock.send(input().encode()))
    while(i < lenghtIndex):
        print(sock.recv(1024).decode())
        sock.send(input().encode())
        data1 = conn.recv(1024)
    data = sock.recv(4096)
    data_arr = json.loads(data.decode())
    print(sock.recv(4096).decode()) 
sock.close()
