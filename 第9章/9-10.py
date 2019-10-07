import os						#导入os模块
dir_list = os.listdir('ostest')		#调用listdir()方法返回“ostest”目录下的文件列表
i=1							#初始化i的值为1
os.chdir('ostest')				#将当前工作目录切换到“ostest”目录下
for name in dir_list:				#遍历列表
    print(name)				#输出原文件名
    new_name = str(i) + name	#在原文件名前加上数字进行编号
    i += 1					#i加1
    print(new_name)			#输出新文件名
    os.rename(name,new_name)	#重命名文件