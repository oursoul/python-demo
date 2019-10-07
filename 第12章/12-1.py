import requests							#导入requests库
#异常处理
try:
    r = requests.get('http://www.bjjqe.com')		#使用get函数打开指定的url
    r.raise_for_status()						#如果状态不是200，则引发异常
    r.encoding = 'utf-8'						#更改编码方式
    print(r.text)							#用字符串的形式显示页面内容
except:
    print("网站连接失败！")				#发生异常则输出“"网站连接失败！”
