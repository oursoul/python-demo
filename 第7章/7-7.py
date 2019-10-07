def printinfo( name, age = 35 ):			#定义函数，打印任何传入的字符串
    print ("名字: ", name)
    print ("年龄: ", age)
    return
#调用printinfo函数
print(printinfo.__defaults__)			#输出函数默认值参数
printinfo("root" ,50)					#显式赋值
print ("------------------------")
printinfo("root" )						#使用默认值参数