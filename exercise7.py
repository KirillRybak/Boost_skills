sum1 = 0
sum2 = 0
s = 0
for i in range(1,101):
    x = i**2
    sum1 += x
print('сумма квадратов:',sum1)
for j in range(1,101):
    s += j
    sum2 = s**2
print('Квадрат суммы:',sum2)
print('Разница:',sum2 - sum1)
