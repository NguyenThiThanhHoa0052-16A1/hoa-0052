#kiểm tra số nguyên tố
print("nhập số")
x=int(input("x="))
if x%1==0 & x%x==0:
    print(x,"là số nguyên tố")
else:
    print(x,"ko phải là số nguyên tố")     