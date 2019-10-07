stu_class = {
    'Mary':['C','Math'], 
    'Jone':['Java','Art'],
    'Lily':['Python'], 
    'Tony':['Python','Mysql','Math']
    }									#定义字典并赋值
for name,cla in stu_class.items():				#遍历字典所有的元素
    print(name,'选的课程是:',)				#输出键
    for c in cla:							#遍历列表
        print(c)							#输出列表中的值
