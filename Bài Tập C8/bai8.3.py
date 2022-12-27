# giải pt bậc nhất
print("cho pt bậc nhất ax+b=0")
a=int(input("a="))
b=int(input("b="))
if a ==0  & b==0:
    print("phương trình có vô số nghiệm")    
if a ==0 & b!=0 :
    print("phương trình vô nghiệm")
else:
    print("phương trình có nghiệm là:" ,-b/a)