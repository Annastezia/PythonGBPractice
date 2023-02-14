my_lst1 = [1, 4, 'zero', 8, 5, 'word', 0]
my_lst2 = [input() for _ in range(int(input('Введите количество элементов: ')))]

def dict(var):
    return {key: value for key, value in zip(var, var)}

print(dict(my_lst1))
print(dict(my_lst2))
