import copy

x = int(input("Enter width: "))     #Запрос длины
y = int(input("Enter high: "))      #Запрос Высоты

x_lst = [0]     #Длина, только в спсике
y_lst = [0]     #Высота,только в списке

for X in range(0,x):    #преобразовыввваем число длины в список с соответствующими значениями
    X=X+1               #ну типо 3 - [1,2,3]
    x_lst.append(X)
for Y in range(0,y):    #преобразовыввваем число высоты в список с соответствующими значениями
    Y=Y+1               #ну типо 3 - [1,2,3]
    y_lst.append(Y)

x_lst_c = copy.deepcopy(x_lst)      #Делаем глубокое копирование списка длины для работы с ним

for k in range(0,x+1):                          #изменяем первую строку копии таблицы для более пряитного отображения
    x_lst_c[k] = str(x_lst_c[k]).rjust(3," ")
    k=k+1
print(*x_lst_c)                                 #выводим копию первой строки таблицы

for l in range(1,y+1):                              #цикл для вывода Y количеста строк
    x_lst_c = copy.deepcopy(x_lst)                  #приводим копию к оригиналу
    for L in range(0,x+1):                              #цикл для изменения значений X под Y
        x_lst_c[L]=x_lst_c[L]*l
        x_lst_c[L] = str(x_lst_c[L]).rjust(3, " ")      #оформление строки
        L=L+1
    x_lst_c[0] = str(l).rjust(3," ")                #изменение+оформление первого столбца
    print(*x_lst_c)
    l=l+1