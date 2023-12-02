#encoding:utf8
import requests
from lxml import etree
import re
dai = ['175.155.25.20:808'] #代理ip
head = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0"} #头的信息

cookie = {'Cookie':'q_c1=42980743158c4aab9d8111f90172ec69|1490747011000|1490747011000; r_cap_id="ZTIxNTU3YWE3NjNmNDY1YmI1NDc2ZTFkZWM4ZWYyNDI=|1493277797|377fb0c22c8ac4f0dd192742d2c7e74f876f4b1b"; cap_id="ZjIwM2NlYTJhOWNiNDIxZjg0NDBkYzEyNTZlZTk3ZWM=|1493277797|cc27229fb1908723c6a19c8acc8f83fc181770a4"; capsion_ticket="2|1:0|10:1492830337|14:capsion_ticket|44:MjJiMTFmNjNlZTVlNDdmMjk3YzAxNjZmMzkwMjkyYmQ=|cfc0184334508f233cda25a1549f9ab8ff3abd2bcde0eb00d57d561b3d37da71"; aliyungf_tc=AQAAAKV5ZgOXbQsAAtD5cpIi0/Ex8fux; acw_tc=AQAAAOfo2CFxJQ0AAtD5cms3yXOcEGH+; _xsrf=aec21e958db4d4c03ed5ba3245ce3eca; d_c0="AJACY2OmqwuPTikw3aZFLtfreGDGHsZiGRw=|1493277794"; l_n_c=1; __utma=51854390.267103839.1493278142.1493278142.1493278142.1; __utmb=51854390.0.10.1493278142; __utmc=51854390; __utmz=51854390.1493278142.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmv=51854390.000--|3=entry_date=20170329=1; _zap=dbcdd0ce-8192-4652-a8b0-dc163795627b; z_c0=Mi4wQUNBQ2R4Umlxd3NBa0FKalk2YXJDeGNBQUFCaEFsVk45Q2twV1FEMmF2aVlHeFpSNlE4bE15YnFyU2xfT0Z2cE1R|1493277941|74ef22a4df0a689b9eb43adcba977aebd9d165e5'}

te = requests.get('https://www.zhihu.com/#signin',cookies=cookie,headers=head,proxies=dai).text
demo = re.compile('<span class="Guide-BioEditorBio">(.*?)</span>',re.S)
aa = demo.findall(te)
print(aa)
