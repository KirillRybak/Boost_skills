prov = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
x = 230000000
while x < 300000000:
    x += 1
    spis = []
    for j in range (1,21):
        if x%j == 0:
            spis.append(j)
            if spis == prov:
                print(x)
                break

        else:
            break





