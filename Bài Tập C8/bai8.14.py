#Tính tổng n số nguyên
n=int(input("nhap n "))
k=0
while n>0:
     print("nhap so thu ",n)
     h=int(input())
     k=k+h
     n-=1
     if n==0:
         print("tong cac so bang",k)
         break