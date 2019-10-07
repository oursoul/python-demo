def fac(k):						#定义fac函数，计算阶乘
    i = 2
    t = 1
    while i <= k:
        t *= i
        i = i + 1
    return t						#返回阶乘结果
def sum(n):						#定义sum函数，求累加
    s = 0
    i = 1
    while i <= n:
        s = s + fac(i)				#调用fac函数
        i += 1
    return s						#返回累加结果
print('1!+2!+3!…10!=',sum(10))		#调用sum函数