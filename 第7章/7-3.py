def demo(s):							#定义函数
    a = 0							#变量a用于存储大写字母个数
    b = 0							#变量b用于存储小写字母个数
    for ch in s:						#循环判断字符串中的每个字母
        if ch.isupper():					#调用isupper()方法判断是否为大写字母
            a += 1					#如果是a加1
        elif ch.islower():				#调用islower()方法判断是否为小写字母
            b += 1					#如果是b加1
    return a,b							#返回a和b的值
s = input('请输入字符串')				#输入字符串
c = demo(s)							#调用函数返回a和b的值给变量c
print(c,type(c))						#输出变量c及变量c的类型
print('大写字母的个数为：',c[0],'，小写字母的个数为：',c[1])	#输出结果
