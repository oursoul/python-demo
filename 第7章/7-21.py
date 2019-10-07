stuInfos=[]                                 #用来保存学生的所有信息
def printMenu():                                #打印功能提示
    print("="*20)
    print(" 学生管理系统V1.0 ")
    print("1.添加学生信息")
    print("2.删除学生信息")
    print("3.显示所有学生信息")
    print("0.退出系统")
    print("="*20)
#添加一个学生信息
def addStuInfo():
    newNum = input("请输入新学生的学号：")    #提示并获取学生的学号
    newName = input("请输入新学生的姓名：")   #提示并获取学生的姓名
    newSex = input("请输入新学生的性别（男/女）：")   #提示并获取学生的性别
    newInfo = {}                                #定义字典
    #赋值
    newInfo['num'] = newNum
    newInfo['name'] = newName
    newInfo['sex'] = newSex
    stuInfos.append(newInfo)                    #将元素添加到列表中
#删除一个学生信息
def delStuInfo(student):
    del_num = input("请输入要删除的学生的学号：")    #提示并获取学生学号
    for stu in student:                         #遍历列表
        if stu['num'] == del_num:               #判断是否与输入的学号相同
            student.remove(stu)                 #删除该学生信息
#定义一个用户显示所有学生信息的函数
def showStuInfo():
    print("=" * 20)
    print("学生的信息如下:")
    print("=" * 20)
    print("序号    学号    姓名   性别")
    i = 1
    #遍历存储学生信息的列表，输出每个学生的详细信息
    for tempInfo in stuInfos:
        print("%d      %s      %s     %s" % (i, tempInfo['num'],tempInfo['name'], tempInfo['sex']))
        i += 1
#main函数控制整个程序的流程
def main():
    while True:
        printMenu()                         #打印功能菜单
        key = input("请输入功能对应的数字")   #获取用户输入
        if key == '1':                          #添加学生信息
            addStuInfo()
        if key == '2':                          #删除学生信息
            delStuInfo(stuInfos) 
        elif key == '3':                            #显示学生信息
            showStuInfo()
        elif key == '0':                            #退出循环
            quit_con = input("确定退出吗？（Yes or No）：")
            if quit_con == 'Yes':
                break
main()
