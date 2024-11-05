import urllib.request
import json

# 서버 URL

url = "http://your-server.com/api/data"

# 보낼 데이터

data = {'S/N': xxxx.xxxx.xxxx, 'isdoor': 1}
json_data = json.dumps(data).encode('utf-8')

# 요청 설정

req = urllib.request.Request(url, data=json_data, headers={'Content-Type': 'application/json'})

# POST 요청 보내기

with urllib.request.urlopen(req) as response:
print(response.read().decode())
