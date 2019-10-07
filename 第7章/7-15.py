num = 1
def fun():
    global num			#使用global关键字声明变量为全局变量
    num += 1
    print('函数内num的值为',num)
fun()
print('函数外num的值为',num)
