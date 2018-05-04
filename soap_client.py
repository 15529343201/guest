# -*- coding=utf-8 -*-
from suds.client import Client
# 使用库 suds_jurko： https://bitbucket.org/jurko/suds
# web service 查询： http://www.webxml.com.cn/zh_cn/web_services.aspx
# 电话号码归属地查询
url = 'http://webservice.webxml.com.cn/WebServices/MobileCodeWS.asmx?wsdl'
client = Client(url)
print(client)

# 使用库 suds_jurko： https://bitbucket.org/jurko/suds
# web service 查询： http://www.webxml.com.cn/zh_cn/web_services.aspx
# 电话号码归属地查询
url = 'http://webservice.webxml.com.cn/WebServices/MobileCodeWS.asmx?wsdl'
client = Client(url)
result = client.service.getMobileCodeInfo(186xxxxxxxx)
print(result)