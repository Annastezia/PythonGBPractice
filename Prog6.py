F = float(input('Enter: '))
sum = 0

for i in range(0,len(str(F))):
    F=F*10
    print(F)
F = int(F)

while F!=0:
    sum = sum + F%10
    F = F//10
print(sum)