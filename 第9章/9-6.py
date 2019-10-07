with open('testfile.txt','r') as file1,open('copy.txt','w') as file2:		#打开两个文件
    file2.write(file1.read())	#将从“testfile.txt”中读取的内容写入到“copy.txt”中
