filename = input('请输入新建的文件名：')		#输入文件名
with open(filename,'w+') as file:				#新建文件并以读写方式打开
    file.write('This is a test!')				#将字符串输入到文件
    file.seek(10)							#指针移到从头开始的第10个字符处
    con = file.read(4)						#读取4个字符给con
    print(con)								#输出
