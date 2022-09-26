x= int(input("Введите координаты x "))
y= int(input("Введите координаты y "))
if x==0 or y==0:
    print("не лежат в какой либо четверти")
elif x>0:
    if y>0:
        print(1)
    else:
        print(2)
else:
    if y>0:
        print(4)
    else:
        print(3)
