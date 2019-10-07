stu_class = {
    'Mary':'C', 
    'Jone':'Java', 
    'Lily':'Python', 
    'Tony':'Python'
    }									#定义字典并赋值
for name, cla in stu_class.items():		#遍历“键-值”对
    print(name,'选修的是',cla)			#输出每个值