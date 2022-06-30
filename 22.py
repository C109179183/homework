c=[]
c.append(["123","456","9000"])
c.append(["456","789","5000"])
c.append(["789","888","6000"])
c.append(["336","558","10000"])
c.append(["775","666","12000"])
c.append(["566","221","7000"])

bb=int(input('輸入查詢組數N為:'))
for i in range(bb):
    sign=input().split(" ")
    for j in range(len(c)):
        if sign[0]==c[j][0] and sign[1]==c[j][1]:
            print(c[j][2])
            break
        else:
            print("error")
            break