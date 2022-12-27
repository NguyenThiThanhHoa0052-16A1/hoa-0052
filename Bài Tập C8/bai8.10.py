<<<<<<< HEAD
#Tính S
a=int(input("nhap n "))
b=int(input("nhap x "))
t=(b*b+1)
i=1
h=1
while i<=a:
     h=h*t
     i+=1
print("S=(x*x+1)^n=",h)
while i>a:
     h=1/(h*t)
     i+=1
=======
#Tính S
a=int(input("nhap n "))
b=int(input("nhap x "))
t=(b*b+1)
i=1
h=1
while i<=a:
     h=h*t
     i+=1
>>>>>>> 7ac7d37118a62ae7874b179cdeb2d9f6739b9a74
print("S=(x*x+1)^n=",h)