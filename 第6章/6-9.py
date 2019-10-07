stu_class = {
    'Mary':'C', 
    'Jone':'Java', 
    'Lily':'Python', 
    'Tony':'Python'
    }			#定义字典并赋值
print('以下课程已被选择：')
for cla in set(stu_class.values()):
				#遍历字典所有的值，调用set()将列表转换为集合从而去除重复项
    print(cla)		#输出每个值
