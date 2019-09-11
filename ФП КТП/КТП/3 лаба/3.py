def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
def function(len):
    mas2=[]
    a = 1
    while(len != 0):
        print("Введите элементы через пробел массива ", len, " глубины")
        str= input()
        if a != 1 :
            mas2.append(mas3)
        mas1 =(str.split(" "))
        for i in mas1:
            if is_number(i) == True:
                 mas2.append(int(i))
        mas3 = mas2
        mas2 = []
        len -= 1
        a += 1
    return mas3
len = int(input("Введите глубину списка\n"))
mas = function(len)
print(mas)
