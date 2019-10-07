def changeme(mylist):
    "修改传入的列表"
    mylist.append([1,2,3,4])
    print("函数内取值: ", mylist)
    return
mylist = [10,20,30]
changeme(mylist)
print ("函数外取值: ",mylist)
