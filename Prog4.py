Q = int(input("Введите номер четверти: "))

if Q == 1:
    print("X>0, Y>0")
elif Q == 2:
    print("X>0, Y<0")
elif Q == 3:
    print("X<0, Y<0")
elif Q == 4:
    print("X<0, Y>0")
else:
    print("Введите число от 1 до 4!")