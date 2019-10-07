with open('testfile.txt','r') as file:	#以只读方式打开原有的名为“testfile.txt”的文件
    line = file.readline()		#读取一行
    print(line)				#输出
    print('*'*30)				#输出30个*用于分隔
    line = file.readline(10)		#读取下一行的前10个字符
    print(line)				#输出

