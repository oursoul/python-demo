file = open('testfile.txt','w')			#打开名为“testfile.txt”的文件
#向文件中输入字符串
file.write('Interface options\n')
file.write('Generic options\n')
file.write('Miscellaneous options\n')
file.write('Options you shouldn’t use\n')
file.close()					#关闭文件
