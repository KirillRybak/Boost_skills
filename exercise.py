sum = 0
n1=1
n2=2
print(n1,end=" ")
while n2<4000000:
    print(n2, end=" ")
    n1,n2=n2,n1+n2
    if n2%2==0:
        sum += n2

print("Рузультат программы: ",sum)


