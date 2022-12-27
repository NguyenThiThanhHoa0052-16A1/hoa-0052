# Tính S
import math
x=int(input('Nhập x:'))
y=int(input('nhập y:'))
if x>=y:
      S=x-y
      print('S =',S)
else: 
      S=math.sqrt(pow(x,2)+pow(y,2))
      print('S =',S)      