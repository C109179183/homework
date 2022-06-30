n = int(input("輸入一正整數:"))
if n >=11 and n<=1000:
    if n%2 == 0 and n%11 ==0 and n%5 != 0 and n%5 != 0:
        print(n,"為新公倍數?:","YES")
    else:
        print(n,"為新公倍數?:","NO")