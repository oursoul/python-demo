import requests						#导入requests库
import re								#导入re模块
from bs4 import BeautifulSoup			#导入BeautifulSoup
#定义一个getHtml()函数，根据填写的url参数获取数据
def getHtml(url):
    #异常处理
    try:
        r = requests.get(url)				#使用get函数打开指定的url
        r.raise_for_status()				#如果状态不是200，则引发异常
        r.encoding = 'utf-8'				#更改编码方式
        return r.text					#返回页面内容
    except:
        return ""						#发生异常返回空字符
#定义数据解析函数，用于找到符合条件的数据并输出
def getcon(html):
    bsObj = BeautifulSoup(html)			#将html对象转化为BeautifulSoup对象
    #找到所有class为bk_show_info的div来只获取图书的信息
    divList = bsObj.find_all('div',{'class':'bk_show_info'}) 
    allbook = []						#存储全部数据，二维列表
    for divs in divList:
        book_info = []					#存储单本图书信息，一维列表
        book_name = divs.h4['data-name']	#获取图书名称
        book_info.append(book_name)	#将图书名称存储到book_info
        p_list = divs.find_all('p')			#查找单本图书的其他信息（在标签p中）
        for p_content in p_list:
    	    book_info.append(p_content.string)	#将p标签中的信息存入book_info
        allbook.append(book_info)		#将单本图书的信息存入allbook
    #输出获取到的图书信息
    for book in allbook:
        print(book)
html = getHtml("http://www.bjjqe.com/")	#调用获取页面内容函数
getcon(html)							#调用解析数据函数
