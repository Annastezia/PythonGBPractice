import random

my_str = [int(random.randint(0, 10)) for i in range(1, 20)]
print(my_str)

def count(my_str):
    dict= {int(item):my_str.count(item) for item in my_str}
    sorted = sorted(dict.items(), key=lambda item: item[1])
    return dict(sorted[-3:])

print(count(my_str))