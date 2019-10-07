with open('testfile.txt','r') as file:	#以只读方式打开原有的名为“testfile.txt”的文件
    line = file.read(8)			#读取前8个字节
    print(line)				#输出前8个字节
    p = file.tell()				#获取指针当前位置
    print('当前位置：',p)		#输出当前位置
    line = file.read(4)			#继续读取4个字节
    print(line)				#输出读取到的数据
    p = file.tell()				#获取指针当前位置
    print('当前位置：',p) 		#输出当前位置
