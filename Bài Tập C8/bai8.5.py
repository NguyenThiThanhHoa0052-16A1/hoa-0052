#ktra nam nhuận
print("nhập năm:")
a=int(input("nam="))
if( (a%4==0) &(a%100!=0)) or (a%400==0):
    print(a," là năm nhuận" )
else:
    print(a ," không phải là năm nhuận")

