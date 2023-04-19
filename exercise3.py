sum = 0
n1 = 3
n2 = 5
i = 0
while i<1000:
    i += 1
    if i%3==0 or i%5==0:
        sum += i
        print(i)
        print('Промежуточный результат сложения',sum)
print('Результат',sum)

#   If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
#   The sum of these multiples is 23.Find the sum of all the multiples of 3 or 5 below 1000.
