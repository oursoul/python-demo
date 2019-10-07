stu_info = {
    'WangMi':{'sex':'F','age':'15'},
    'LinMei':{'sex':'M','age':'14'},
    'ChenHui':{'sex':'F','age':'14'}
}										#定义字典并赋值
for name, stu in stu_info.items():		#遍历字典所有元素
    print(name,'性别',stu['sex'],'年龄',stu['age'])	#输出键和值