def hello():
    for i in range(100,1000):
        for j in range(100,1000):
            num = i*j
            end_num = num

            pol = 0
            while num>0:
                x=num%10
                pol=pol*10+x
                num=num//10
                if pol == end_num:
                    print(i,'*',j,'=',end_num)

hello()



