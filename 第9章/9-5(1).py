with open('testfile.txt','r') as file:	#以只读方式打开原有的名为“testfile.txt”的文件
    content = file.readlines()		#读取所有行并返回列表
print(content)					#输出列表
print('*'*60)					#输出60个*用于分隔
for temp in content:				#遍历列表
	print(temp)				#输出列表每个元素
