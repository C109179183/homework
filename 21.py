data = [["123","neo"],["456","john"],["789","amy"],["321","Lim DBA"],["654","ken"]]
i = input("請輸入學生學號 : ")

for j in range(len(data)):
    if i == data[j][0]:
        print("學生資料為",i,data[j][1])
    else:
        print("輸入錯誤")