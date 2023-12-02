import requests
from bs4 import BeautifulSoup

# 登录页面的URL
login_url = 'http://yy.jdyfy.com/manage/v1/api/web/doc/unauth/login-by-password?t=2&courtyardCode=YQ01'

# 要提交的用户名和密码
usernameOrPhone = '18042207177'
password = 'Zinanc613613'

# 创建一个会话（Session）来处理登录会话
with requests.Session() as session:
    # 发送GET请求，获取登录页面的CSRF令牌或其他必要的信息
    # response = session.post(login_url)

    # 如果有CSRF令牌等信息，可以从响应内容中提取

    # 构建POST请求的数据，包括用户名和密码
    login_data = {
        'usernameOrPhone': usernameOrPhone,
        'password': password
        # 还可以包括其他登录所需的字段
    }

    # 发送POST请求进行登录
    resp = session.post(login_url, data=login_data)
    # resp.encoding = 'utf-8'
    # print(resp.text)
    resp = session.get('http://yy.jdyfy.com/manage/v1/url/config/unapiauth/query/bytype?type=request-encrypt')
    print(resp)
    resp = session.get('http://yy.jdyfy.com/patient/v1/offline/regist/unauth/date?courtyardCode=YQ01')
    print(resp)

