str1 = input("Введите текст\n")
str1= str1.strip()
des = ''
while(str1 != ''):
    for i in str1:
        if i == ' ':
            a = True
    if a == True:
        n = str1.index(' ')
    else:
        n = len(str1)
    str2 = str1[0:n+1:]
    if str2.istitle() == True:
        str2 = str2.upper()
    des += str2
    str1 = str1[n+1:len(str1):]
    a = False
print(des)

