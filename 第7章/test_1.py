def minimal(x, y):						#自定义计算较小值函数
    if x > y:							#如果x>y成立，返回y的值
        return y
    else:								#否则返回x的值
        return x
#用来测试
if __name__ == '__main__':				#识别当前的运行方式
    r = minimal(2,3)
    print('测试2和3的较小值为:',r)