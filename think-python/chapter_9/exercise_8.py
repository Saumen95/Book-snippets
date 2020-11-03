for i in range(1000000):
    miles1 = str(i).zfill(6)
    miles2 = str(i+1).zfill(6)
    miles3 = str(i+2).zfill(6)
    miles4 = str(i+3).zfill(6)
    if miles1[2:6] == miles1[2:6][::-1]:
        if miles2[1:6] == miles2[1:6][::-1]:
            if miles3[1:5] == miles3[1:5][::-1]:
                if miles4 == miles4[::-1]:
                    print(miles1, miles2, miles3, miles4)