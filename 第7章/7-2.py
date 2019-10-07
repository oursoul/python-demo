def minimal(x, y):						#自定义计算较小值函数
    if x > y:							#如果x>y成立，返回y的值
        return y
    else:								#否则返回x的值
        return x
a = float(input('输入第一个数据：'))		#输入a的值
b = float(input('输入第二个数据：'))		#输入b的值
c = minimal(a, b)						#调用函数，将较小值赋给c
print('较小值为：',c)					#输出c的值
