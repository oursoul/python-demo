with open('seek.txt','rb') as file:			#新建文件并以读写方式打开
    file.seek(-2,2)						#将文件位置指针定位到倒数第2个字符处
    con = file.read(1)					#读取1个字符给con
    print(con)							#输出