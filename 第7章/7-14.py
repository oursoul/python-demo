total = 0 								#全局变量total
def sum( arg1, arg2 ):					#返回2个参数的和
    total = arg1 + arg2					#局部变量total
    print ("函数内是局部变量 : ", total)	#输出局部变量total的值
    return total
sum(10, 20)							#调用sum函数
print ("函数外是全局变量 : ", total)		#输出全局变量total的值