with open('testfile.txt','r') as file:	#以只读方式打开原有的名为“testfile.txt”的文件
    line = file.read(10)			#读取前10个字节
    print(line)				#输出前10个字节
    print('*'*30)				#输出30个*用于分隔
    content = file.read()			#读取文件中剩余的所有内容
    print(content)				#输出
