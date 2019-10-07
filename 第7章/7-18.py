import test                                 #导入test模块
a = float(input('输入第一个数据：'))        #输入a的值
b = float(input('输入第二个数据：'))        #输入b的值
c = test.minimal(a, b)                       #调用函数，将较小值赋给c
print('较小值为：',c)                    #输出c的值
