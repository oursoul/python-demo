stu_info1 = {'num':'20180101', 'name':'Liming', 'sex':'male'}
										#直接赋值创建字典
stu_info2 = dict(stu_info1)					#通过其他字典创建
stu_info3 = dict([('num', '20180101'), ('name', 'Liming'), ('sex', 'male')])
										#通过“(键,值)”对的序列创建
stu_info4 = dict(num = '20180101', name = 'Liming', sex = 'male')
										#通过关键字参数创建
stu_info5 = dict(zip(['num', 'name', 'sex'], ['20180101', 'Liming', 'male']))
										#通过dict和zip结合创建
if stu_info1 == stu_info2 == stu_info3 == stu_info4 == stu_info5:
										#判断五个变量是否相等
    print("创建字典的5种方式相同")		#如果相同输出提示符
else:										#如果不相同
    print("创建字典的5种方式不相同")		#输出提示符
