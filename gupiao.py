# coding:utf8
import re  # 匹配正则表达式
import \
    requests  # Requests 使用的是 urllib3，因此继承了它的所有特性。Requests 支持 HTTP 连接保持和连接池，支持使用 cookie 保持会话，支持文件上传，支持自动确定响应内容的编码，支持国际化的 URL 和 POST 数据自动编码。
import time  # 时间模块
import mysql.connector  # 引入数据库模块 ，connect是存入数据
from selenium import webdriver  # selenium是web自动化测试工具集，包括WebDriver（selenium 2.0）等。 #webdriver 操作浏览器

# （注：）WebDriver 通过原生浏览器支持或者浏览器扩展直接控制浏览器。WebDriver 针对各个浏览器而开发，取代了嵌入到被测 Web 应用中的 JavaScript。


# url = http://quote.stockstar.com/stock/ranklist_a_3_1_1.html  #网站地址
db = mysql.connector.connect(user='root', password='12345678', host='127.0.0.1', port=3306, db='233')
cursor = db.cursor()
driver = webdriver.PhantomJS()  # 驱动Phjs浏览器
demo = re.compile(
    '<tr><td.*?><a.*?>(.*?)</a></td><td.*?><a.*?>(.*?)</a></td><td.*?><span.*?>(.*?)</span></td><td.*?><span.*?>(.*?)</span></td><td.*?><span.*?>(.*?)</span></td><td.*?><span.*?>(.*?)</span></td><td.*?>(.*?)</td><td.*?>(.*?)</td><td.*?>(.*?)</td><td.*?>(.*?)</td><td.*?>(.*?)</td><td.*?>(.*?)</td><td.*?>(.*?)</td></tr>',
    re.S)
while True:  # 此处死循环是为了让数据实时更新
    time.sleep(4)  # 隔4秒更新一次数据
    for i in range(1, 108):  # 获取1-107页的URL地址
        url_a = "http://quote.stockstar.com/stock/ranklist_a_3_1_"
        urls = url_a + str(i) + ".html"

　　　　time.sleep(3)  # 让页面缓存3秒
driver.get(urls)  # 地址以js浏览器提交
yuan = driver.page_source  # 获取源代码
lists = demo.findall(yuan)  # 正则匹配源码
# print(lists)

for a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13 in lists:  # 循环遍历
    # print(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13)
    print('查询--------')
    sql = "select exists(select 1 from shengu where a1='" + a1 + "')"  # 查询数据库里有没有相对应的字段
    cursor.execute(sql)
    listss = cursor.fetchall()  # 游标获取遍历后的数据
    # print(listss[0][0])
    if not listss[0][0]:
        print('插入--------')
        sql1 = "insert into shengu(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13)VALUES ('" + a1 + "','" + a2 + "','" + a3 + "','" + a4 + "','" + a5 + "','" + a6 + "','" + a7 + "','" + a8 + "','" + a9 + "','" + a10 + "','" + a11 + "','" + a12 + "','" + a13 + "')"
        cursor.execute(sql1)
        db.commit()
    else:
        print('更新---------')
        sql2 = "update shengu set a1='" + a1 + "',a2='" + a2 + "',a3='" + a3 + "',a4='" + a4 + "',a5='" + a5 + "',a6='" + a6 + "',a7='" + a7 + "',a8='" + a8 + "',a9='" + a9 + "',a10='" + a10 + "',a11='" + a11 + "',a12='" + a12 + "',a13='" + a13 + "' where a1='" + a1 + "'"
        cursor.execute(sql2)
        db.commit()

# 经测试代码有效