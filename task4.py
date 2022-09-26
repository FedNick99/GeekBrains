from contextlib import nullcontext


numofquater = int(input("Введите номер четверти "))
if numofquater == 1:
    print("x>0,y>0")
elif numofquater == 2:
    print("x>0,y<0")
elif numofquater == 3:
    print("x<0,y<0")
elif numofquater == 4:
    print("x<0,y>0")
else:
    print("такой четверти не существует")