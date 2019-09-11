import socket,json

sock = socket.socket()
sock.bind(('',9091))
sock.listen(1)
conn, addr = sock.accept()
mas = []
i = 0
posN=0
negN=0
a = True
while a == True:
    conn.send('Введите количество элементов массива(длину массива)'.encode())
    lenght = int(conn.recv(1024).decode())
    while i<lenght:
        conn.send("Введите элемент массива".encode())
        mas.append(int(conn.recv(1024).decode()))
        i+=1
        if mas[-1]>=0:
            posN += 1
        else:
            negN += 1
    conn.send("\nВыберите дальнейшие действия:\n 1)Если нужно найти максимальные значения нажмите 1 \n 2)Если нужно найти значения по индексам нажмите 0".encode())
    choice = int(conn.recv(1024).decode())
    def MAX(mas,lenght):
        pro=1
        conn.send("\nВведите количество максимальных значений(которых требуется найти)".encode())
        maxN = int(conn.recv(1024).decode())
        for j in range(lenght-1):
            i=j+1
            while(i!=lenght):
                if mas[j]<mas[i]:
                    a=mas[j]
                    mas[j]=mas[i]
                    mas[i]=a
                i+=1
            if j == (lenght-2):
                conn.send("\nИтог:\nМаксимальные значения - ".encode())
        data_string = json.dumps(mas[0:maxN:])
        conn.send(data_string.encode())
        while maxN>0:
            pro*= mas[maxN-1]
            maxN-=1
        return pro

    def INDEX(mas):
        pro=1
        Index=[]
        conn.send("\nВведите количесвто индексов".encode())
        lenghtIndex = int(conn.recv(1024).decode())
        i = 0
        while i<lenghtIndex:
            conn.send("Введите индекс".encode())
            Index.append(int(conn.recv(1024).decode()))
            Index[-1]= mas[Index[-1]]
            pro*=Index[-1]
            if i == (lenghtIndex-1):
                conn.send("\nИтог:\nЗначения по индексам : ".encode())
            i+=1
        data_string = json.dumps(Index)
        conn.send(data_string.encode())
        return pro

    if choice == 1:
        pro =MAX(mas,lenght)
        conn.send("\nПроизведение чисел :  ".encode())
        conn.send(str(pro).encode())
    elif choice == 0:
        pro=INDEX(mas)
        conn.send("\nПроизведение чисел : ".encode())              
        conn.send(str(pro).encode())
    conn.send("\nДлина массива : ".encode())
    conn.send(str(lenght).encode())
    conn.send("\nКоличество положительных значений массива : ".encode())                      
    conn.send(str(posN).encode())
    conn.send("\nКоличество отрицательных значений массива : ".encode())
    conn.send(str(negN).encode())
    conn.send("\n".encode())
    a=False
conn.close()
