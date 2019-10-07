data = {
    '北京': {
        '昌平': {
            '沙河': ['oldboy', 'test'],
            '天通苑': ['链家地产', '我爱我家']
        },
        '朝阳': {
            '望京': ['奔驰', '陌陌'],
            '国贸': ['CICC', 'HP'],
            '东直门': ['Advent', '飞信']
        },
        '海淀': {},
    },
    '山东': {
        '德州': {},
        '青岛': {},
        '济南': {},
    },
    '广东': {
        '东莞': {},
        '常熟': {},
        '佛山': {},
    },
}
while True:
    for i in data:                      #打印省级列表
        print(i)
    choice = input("请选择城市(退出请按q):")
    if choice in data:                  #如果在省级列表里则进入区县
        while True:
            for i2 in data[choice]:     #打印区县列表
                print(i2)
            choice2 = input("请选择区县(退出请按q返回城市列表请按b):")
            if choice2 in data[choice]: #如果在区县列表里则进去下一级
                while True:
                    for i3 in data[choice][choice2]:    #打印街道列表
                        print(i3)
                    choice3=input("请选择街道(退出请按q返回区县列表请按b):")
                    if choice3 in data[choice][choice2]:
                        for i4 in data[choice][choice2][choice3]:
                            print(i4)
                        choice4 = input("\n已经到达最后一级(退出请按q返回街道列表请按b):")
                        if choice4 == 'b':
                            continue
                        elif choice4 == 'q':
                            exit()
                    elif choice3 == 'b':        #从街道返回区县
                        break
                    elif choice3 == 'q':
                        exit()
            elif choice2 == 'b':                #从区县返回城市
                break
            elif choice2 == 'q':
                exit()
    elif choice == 'q':
        exit()
