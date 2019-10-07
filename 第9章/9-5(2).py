with open('testfile.txt','r') as file:	#以只读方式打开原有的名为“testfile.txt”的文件
    for line in file:					#遍历文件的所有行
    	print(line)						#输出行
