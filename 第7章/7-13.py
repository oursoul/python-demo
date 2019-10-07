def f(n):								#定义递归函数
    if n==1:							#当n等于1时返回1
        return 1
    else:								#当n不为1是返回f(n-1)*n
        return f(n-1)*n
n = int(input('请输入一个正整数：'))		#输入一个整数
print(n,'的阶乘结果为：',f(n))			#调用函数f并输出结果