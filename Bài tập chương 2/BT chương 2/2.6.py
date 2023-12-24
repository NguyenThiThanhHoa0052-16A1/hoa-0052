import json

data='{"name":"Nguyễn Văn A", "age": 19, "city":"Hà Tĩnh","phone": "0365567389"}'

my_data=json.loads(data)

print("Đối tượng Python từ dữ liệu JSON:", my_data)
print("Tên:", my_data['name'])
print("Tuổi:", my_data['age'])
print("Thành phố:", my_data['city'])
print("Số điện thoại:",my_data['phone'])