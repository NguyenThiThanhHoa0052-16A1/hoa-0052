import json

data='{"name":"Nguyễn Văn A", "age": 19, "city":"Hà Tĩnh","phone": "0365567389"}'

json_data=json.dumps(data,indent=4)
print("Chuỗi JSON từ đối tượng Python:",json_data)
