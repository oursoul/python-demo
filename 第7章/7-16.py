def outer():
    num = 1
    def inner():
        nonlocal num			#nonlocal关键字声明
        num = 2
        print(' inner函数中num的值为',num)
    inner()
    print(' outer函数中num的值为',num)
outer()
