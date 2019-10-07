import jieba                            #导入jieba库
excludes = {"将军","却说","主公","荆州","二人","不可","不能","如此"}        #词库
with open("三国演义.txt", "r")as file:
    txt =file.read()                        #打开文件并读取文件内容
words = jieba.lcut(txt)                 #进行分词，将结果放入words列表中
counts = {}                         #定义字典用于存储词语和计数器
for word in words:                      #遍历words
    if len(word) == 1:                  #排除单个字符的分词结果
        continue
#同一人物不同名字的处理功能
    elif word == "诸葛亮" or word == "孔明曰":
        rword = "孔明"
    elif word == "关公" or word == "云长":
        rword = "关羽"
    elif word == "玄德" or word == "玄德曰":
        rword = "刘备"
    elif word == "孟德" or word == "丞相":
        rword = "曹操"
    else:
        rword = word
    counts[rword] = counts.get(rword,0) + 1     #计数器累加
for word in excludes:                           #排除词库中内容
    del(counts[word])
items = list(counts.items())                        #将字典元素转换为列表
items.sort(key=lambda x:x[1], reverse=True)         #排序
for i in range(5):                              #输出前5项
    word, count = items[i]
    print ("{0:<10}{1:>5}".format(word, count))
