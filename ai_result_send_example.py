import requests


url = "http://192.168.55.168:8000/developer_page/recieve_result"


#테스트 데이터1
'''
data = {
    'success': {'installer.exe': 12.68},
    'fail': []
}
'''



# 테스트 데이터2

data = {
    'success': {'soft/tmp_a/file1.exe': 13.21, 'soft/file4.exe': 10.15, 'soft/file5.dll': 5.21, 'soft/file6.dll': 14.21},
    'fail': ['soft/tmp_b/file2.txt', 'soft/tmp_b/file3.png']
}



# JSON 데이터로 전송
response = requests.post(url, json=data)

# 응답 확인
print(response.status_code)
print(response.json())
