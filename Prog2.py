X = int(input("Введите значение X: "))
Y = int(input("Введите значение Y: "))
Z = int(input("Введите значение Z: "))

if (not (X + Y + Z)) == ((not X) * (not Y) * (not Z)):
    print("True")
else:
    print("False")