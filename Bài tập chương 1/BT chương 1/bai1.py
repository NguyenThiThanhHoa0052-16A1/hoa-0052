class ChuNhat:
    length = 0.0
    width = 0.0
    def __init__(self,length = float(input('chiều dài: ')),width = float(input('chiều rộng:'))) :     
        self.length = length
        self.width = width
        
    def perimeter(self):
        print('chu vi hình chữ nhật là: ',(self.length+self.width)*2)

    def acreage(self):
        print('diện tích hình chữ nhật là: ',self.length*self.width)



Thong_so = ChuNhat()
Thong_so.perimeter()
Thong_so.acreage()
