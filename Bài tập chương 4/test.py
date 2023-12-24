import math
r=int(input("Nhập bán kính :"))
CV=0
S=0
def chu_vi(r):
    CV=2*r*math.pi
    return CV
def dien_tich(r):
    S=r*r*math.pi 
    return S 
print("Chu vi:",chu_vi(r))
print("Diện tích:",dien_tich(r))