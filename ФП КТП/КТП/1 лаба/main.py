mas = []
lenght = int(input("Введите количество элементов массива(длину массива)\n"))
print(' ')
i = 0
posN=0
negN=0
while i<lenght:
    print("Введите",i,"элемент массива")
    mas.append(int(input()))
    i+=1
    if mas[-1]>=0:
        posN += 1
    else:
        negN += 1

choice = int(input("\nВыберите дальнейшие действия:\n 1)Если нужно найти максимальные значения нажмите 1 \n 2)Если нужно найти значения по индексам нажмите 0\n"))


def MAX(mas,lenght):
    pro=1
    maxN = int(input("\nВведите количество максимальных значений(которых требуется найти)\n"))
    for j in range(lenght-1):
        i=j+1
        while(i!=lenght):
            if mas[j]<mas[i]:
                a=mas[j]
                mas[j]=mas[i]
                mas[i]=a
            i+=1
    print("\nИтог:\nМаксимальные значения - ", mas[0:maxN:])
    while maxN>0:
        pro*= mas[maxN-1]
        maxN-=1
    return pro

def INDEX(mas):
    pro=1
    Index=[]
    lenghtIndex = int(input("\nВведите количесвто индексов\n"))
    i = 0
    while i<lenghtIndex:
        print("Введите",i+1,"индекс")
        Index.append(int(input()))
        i+=1
        Index[-1]= mas[Index[-1]]
        pro*=Index[-1]
    print("\nИтог:\nЗначения по индексам - ",Index)
    return pro


if choice == 1:
    pro =MAX(mas,lenght)
    print("Произведение чисел - ",pro)
elif choice == 0:
    pro=INDEX(mas)
    print("Произведение чисел - ",pro)
print("Длина массива - ",lenght,"\nКоличество положительных значений массива - ",posN,"\nКоличество отрицательных значений массива - ",negN)
          
####
 def MAX(mas,lenght):
        pro=1
        conn.send("Введите количество максимальных значений(которых требуется найти)\n".encode())
        maxN = int(conn.recv(1024).decode())
        for j in range(lenght-1):
            i=j+1
            while(i!=lenght):
                if mas[j]<mas[i]:
                    a=mas[j]
                    mas[j]=mas[i]
                    mas[i]=a
                i+=1
        conn.send("\nИтог:\nМаксимальные значения - ".encode())
        conn.send(mas[0:maxN:].encode())
        while maxN>0:
            pro*= mas[maxN-1]
            maxN-=1
        return pro

    def INDEX(mas):
        pro=1
        Index=[]
        conn.send("\nВведите количесвто индексов\n".encode())
        lenghtIndex = int(conn.recv(1024).decode())
        i = 0
        while i<lenghtIndex:
            conn.send("Введите индекс".encode())
            Index.append(int(conn.recv(1024).decode()))
            i+=1
            Index[-1]= mas[Index[-1]]
            pro*=Index[-1]
        conn.send("\nИтог:\nЗначения по индексам - ".encode())
        conn.send(Index.encode())
        return pro

    if choice == 1:
        pro =MAX(mas,lenght)
        conn.send("Произведение чисел - ".encode())
        conn.send(pro.encode())
    elif choice == 0:
        pro=INDEX(mas)
        conn.send("Произведение чисел - ".encode())              
        conn.send(pro.encode())
    conn.send("Длина массива -")
    conn.send(lenght)
    conn.send("\nКоличество положительных значений массива - ")                      
    conn.send(posN)
    conn.send("\nКоличество отрицательных значений массива - ")
    conn.send(negN)   
