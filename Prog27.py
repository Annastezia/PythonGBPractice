dict = {'first_one':'we can do it'}

def biggest_dict(**kwargs):
    dict.update(**kwargs)

biggest_dict(second = 2, third = 3, fourth = 4)
print(dict)