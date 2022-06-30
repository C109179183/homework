a = {"1":72,"2":62,"3":82,"4":44,"5":60}
b = {"A":55,"B":68}
cs1 = input("請選擇主餐及升級的套餐:(以空白鍵區隔)")
cs2 = input("是否升級成大杯飲料:")
cs3 = input("是否換成大薯:")
cs = cs1.split()
sum = a[cs[0]]+b[cs[1]]
if cs2 == "是":
    sum = sum + 7
if cs3 == "是":
    sum = sum + 13    
print("總共為",sum,"元")