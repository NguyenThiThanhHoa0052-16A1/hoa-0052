#Tính diện tích tam giác
import math
print("cho số đo 3 cạnh a,b,c")
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
p=(a+b+c)/2
S=math.sqrt(p*(p-a)*(p-b)*(p-c))
print("diện tích của tam giác là:" ,S)