import requests #导入requests包

headers = {
    "User-Agent": "123"
}
response = requests.get("http://yy.jdyfy.com", headers=headers)
url = 'http://yy.jdyfy.com/login'
# response.encoding = 'utf-8'
# print(response.text)