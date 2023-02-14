number = int(input("Введите цифру: "))

if number in range(1,6):
    print("Нет. Выбранный день - будний.")
elif number in range(6,8):
    print("Да. Выбранный день - выходной.")
else:
    print("Нет. Введите число от 1 до 7!")