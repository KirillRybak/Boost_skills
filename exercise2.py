num = 600851475143
j = 2
while True:
    if num%j==0:
        print("Делитель числа: ",j)
        num/=j
        if num==1:
            print("Самый большой простой делитель: ", j)
            break
    j = j+1
