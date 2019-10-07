count =0										#定义count变量并赋初值为0
passwd=123									#定义passwd变量并赋初值为123
dict1={'alex':[passwd,count],'Tom':[passwd,count]}	#定义字典用于存储用户信息
while True:									#开始循环
    name = input("please input your name:")		#输入用户名
    password = int(input("please input your password:"))	#输入密码
    if name not in dict1.keys():					#如果输入的用户名不在字典中
        print("name %s is not in dict"%name)		#输出提示语
        break								#跳出循环
    if dict1[name][1] > 2:						#如果次数大于2
        print("the name %s locked"%name)		#输出被锁定提示信息
        break								#跳出循环
    if password == dict1[name][0]:				#如果输入的密码正确
        print("login ok")						#输出登录成功提示语
        break								#跳出循环
    else:										#密码输入错误
        print("name or passwd error")			#输出提示语
        dict1[name][1] +=1						#次数加1
