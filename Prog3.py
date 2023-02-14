X = int(input("Введите значение X: "))
Y = int(input("Введите значение Y: "))

if X>0 and Y>0:
    print("1 четверть")
elif X>0 and Y<0:
    print("2 четверть")
elif X<0 and Y<0:
    print("3 четверть")
elif X<0 and Y>0:
    print("4 четверть")
else:
    print("Введите X и Y не равные 0!")