N = int(input("Enter number: "))
dict = { }
sum = 0
for i in range(1,N+1):
    dict[i] = (1 + (1/i))**i
    sum = sum + dict[i]
print(dict)
print(sum)