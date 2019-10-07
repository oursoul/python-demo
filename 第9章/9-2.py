ls = ['Environment\n','variables']	#定义列表并赋值
with open('testfile.txt','a') as file:	#以追加方式打开原有的名为“testfile.txt”的文件
    file.writelines(ls)			#向文件中追加字符串列表
