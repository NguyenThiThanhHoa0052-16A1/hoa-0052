class PS:
    def __init__(self):
        self.tu_so = int(input("nhập tử số: "))
        self.mau_so = int(input("nhập mẫu số"))
    def test (self):
        if self.mau_so == 0 or self.tu_so == 0:
            return False
        return True
    def out(self):
        print(f'{self.tu_so}/{self.mau_so}')

Phan_so = PS()
if Phan_so.test() == True:
    Phan_so.out()
else:
    print("phân số không hợp lệ")